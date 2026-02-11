import streamlit as st

from config.settings import IMAGE_SIZE
from inference.load_model import load_models

from ui.sidebar import render_sidebar
from ui.home import render as home_page
from ui.display import render_main_ui
from ui.detection import render as detection_page

# Konfigurasi halaman
st.set_page_config(
    page_title="Tomato Ripeness Classification",
    page_icon="🍅",
    layout="centered"
)
page = render_sidebar()

@st.cache_resource
def load_cached_model():
    return load_models()

model, class_labels = load_cached_model()

# Routing halaman
if page == "🏠 Home":
    home_page()

elif page == "📊 Klasifikasi":
    st.title("🍅 Klasifikasi Tingkat Kematangan Buah Tomat")
    render_main_ui(model, IMAGE_SIZE, class_labels)

elif page == "🎯 Detection":
    detection_page()
