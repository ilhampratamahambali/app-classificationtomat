# config/settings.py

IMAGE_SIZE = (500, 500)

MODEL_PATHS = {
    "svm": "models/svm.joblib",
    "feature_names": "models/feature_names.parquet",
    "class_labels": "models/class_labels.joblib"
}

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]
