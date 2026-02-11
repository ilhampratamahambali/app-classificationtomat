import streamlit as st

def render_sidebar():
    st.sidebar.title("🍅 Tomato Ripeness")
    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "📌 Menu",
        [
            "🏠 Home",
            "📊 Klasifikasi",
            "🎯 Detection"
        ]
    )

    return page
