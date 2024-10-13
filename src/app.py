import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Made in America', layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("src/style/style.css")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown('<div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["Employment Trends", "Industry Comparison", "Geographic Map"])

    st.image("src/visuals/gm_hq.png", width=860)
    st.markdown("""
        ### An American Comeback
        """)
    st.markdown('</div>', unsafe_allow_html=True)
