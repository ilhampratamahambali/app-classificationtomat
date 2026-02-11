import joblib
import pandas as pd
from config.settings import MODEL_PATHS


def load_models():
    # Load SVM model
    model = joblib.load(MODEL_PATHS["svm"])

    # Load class labels (dict / list)
    class_labels = joblib.load(MODEL_PATHS["class_labels"])


    print("Loaded model:", type(model))
    print("Class labels:", class_labels)

    return model, class_labels
