import streamlit as st

from preprocessing.image_loader import load_image
from preprocessing.image_preprocessing import crop_and_segment_tomato
from preprocessing.feature_extraction import extract_all_features
from inference.classifier import predict
from utils.helpers import label_description


def render_main_ui(model,  IMAGE_SIZE, class_labels):
    st.subheader("📊 Klasifikasi Kematangan Tomat")

    uploaded = st.file_uploader(
        "Upload gambar tomat",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded is not None:
        try:
            image = load_image(uploaded)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(image, caption="Gambar Tomat", channels="BGR")

            if st.button("🔍 Klasifikasi"):
                segmented = crop_and_segment_tomato(image, IMAGE_SIZE)
                features = extract_all_features(segmented)
                result = predict(features, model, class_labels)

                st.success(f"Tingkat Kematangan: **{result}**")
                st.info(label_description(result))

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
