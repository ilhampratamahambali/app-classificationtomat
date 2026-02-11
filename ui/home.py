import streamlit as st

def render():
    st.title("🍅 Klasifikasi Tingkat Kematangan Buah Tomat")

    st.markdown("""
    ### 📌 Deskripsi Proyek
    Aplikasi ini bertujuan untuk mengklasifikasikan tingkat
    kematangan buah tomat berdasarkan citra digital.

    ### 🧠 Metode yang Digunakan
    - Ekstraksi fitur tekstur **GLCM**
    - Ekstraksi fitur warna **Color Moment**
    - Klasifikasi menggunakan **Support Vector Machine (SVM)**

    ### 🎯 Kategori Kematangan
    - Mentah  
    - Setengah Matang  
    - Matang  

    ### 🚀 Pengembangan Selanjutnya
    - Deteksi tomat otomatis menggunakan YOLO
    - Integrasi deteksi dan klasifikasi kematangan
    """)
