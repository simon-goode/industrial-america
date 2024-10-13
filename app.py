import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Made in America', layout="wide")

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), url(https://media-cldnry.s-nbcnews.com/image/upload/streams/2014/February/140203/2D11495359-140203-manufacturing-1129.jpg);
        min-height: 100vh;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }

    .middle-column {
        background-color: white;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
# left_col, mid_col, right_col = st.columns([1, 3, 1])
st.markdown('<div class="middle-column">', unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Employment Trends", "Industry Comparison", "Geographic Map"])

st.image("visuals/gm_hq.png", use_column_width=True)
st.markdown("""
    ### An American Comeback
""")

st.markdown('</div>', unsafe_allow_html=True)