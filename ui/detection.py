import streamlit as st

def render():
    st.title("🎯 Deteksi Tomat")

    st.warning("""
    Fitur deteksi tomat masih dalam tahap pengembangan.

    Rencana:
    - YOLO untuk mendeteksi tomat
    - Crop hasil deteksi
    - Klasifikasi kematangan menggunakan SVM
    """)
