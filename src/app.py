import streamlit as st
import plotly.express as px
import pandas as pd
from scripts.parse import *

st.set_page_config(page_title='Made in America', layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("src/style/style.css")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.link_button("Donate", url="https://secure.actblue.com/donate/web-donate")

with col2:
    st.markdown('<div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Overview", "2007-2016", ".", "..", "...", "About"])

    # overview
    with tab1:
        st.image("src/visuals/gm_hq.png", width=860)
        st.markdown("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sit amet convallis ligula. Pellentesque quis malesuada elit, ut varius arcu. Duis sollicitudin, nibh id sodales finibus, augue arcu venenatis sapien, in accumsan lectus magna id metus. Etiam rutrum dictum efficitur. Quisque mattis velit eu erat eleifend tempus. In nec varius massa. Nunc et rhoncus velit. Suspendisse fringilla turpis non nulla condimentum ullamcorper. Aliquam eu odio id quam luctus elementum.
        """)

        year = st.slider("Year:", 2004, 2020, step=4)
        st.plotly_chart(plot_vote_margin_diff(year))

        st.markdown('</div>', unsafe_allow_html=True)

    # about
    with tab6:
        st.markdown("""
            Heya, I'm Simon Goode, a student at Brandeis University studying Applied Math and Economics.
            
            [LinkedIn](https://www.linkedin.com/in/simon-goode-25581324a/)
            [GitHub](https://github.com/simon-goode/industrial-america)
                    """)