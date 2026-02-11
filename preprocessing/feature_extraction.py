import numpy as np
import cv2
from skimage.feature import graycomatrix, graycoprops
from scipy.stats import skew
from preprocessing.image_preprocessing import to_gray, to_hsv

def extract_glcm_features(gray_image):
    distances = [1, 2]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]

    glcm = graycomatrix(
        gray_image.astype(np.uint8),
        distances=distances,
        angles=angles,
        levels=256,
        symmetric=True,
        normed=True
    )

    features = []
    for prop in ["contrast", "dissimilarity", "homogeneity",
                 "energy", "correlation", "ASM"]:
        features.append(graycoprops(glcm, prop).mean())

    return features

def extract_color_moments(hsv_image):
    features = []
    for channel in cv2.split(hsv_image):
        flat = channel.flatten()
        mean = np.mean(flat)
        std = np.std(flat)
        skewness = skew(flat) if std > 1e-6 else 0.0
        features.extend([mean, std, skewness])
    return features

def extract_all_features(image):
    gray = to_gray(image)
    hsv = to_hsv(image)

    glcm = extract_glcm_features(gray)
    color = extract_color_moments(hsv)

    return np.array(glcm + color).reshape(1, -1)
