import streamlit as st
import plotly.express as px
import pandas as pd
from scripts.parse_chart1 import *

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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Overview", "Dismantled", "Donald Trump", "Joe Biden", "The Future", "About"])

    # overview
    with tab1:

        st.image("src/visuals/gm_hq.png", width=860)
        st.markdown("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sit amet convallis ligula. Pellentesque quis malesuada elit, ut varius arcu. Duis sollicitudin, nibh id sodales finibus, augue arcu venenatis sapien, in accumsan lectus magna id metus. Etiam rutrum dictum efficitur. Quisque mattis velit eu erat eleifend tempus. In nec varius massa. Nunc et rhoncus velit. Suspendisse fringilla turpis non nulla condimentum ullamcorper. Aliquam eu odio id quam luctus elementum.
        """)

        # vote margin differential from previous election, by county
        year = st.slider("Year:", 2004, 2020, step=4)
        # st.image(f"src/visuals/chart1/{year}.png", use_column_width=True)
        st.plotly_chart(get_vote_margin_diff(year))

        st.markdown('</div>', unsafe_allow_html=True)

    # about
    with tab6:
        st.markdown("""
            Hi there, I'm Simon Goode, a student at Brandeis University studying Applied Math and Economics.
            
            [LinkedIn](https://www.linkedin.com/in/simon-goode-25581324a/)
            [GitHub](https://github.com/simon-goode/industrial-america)
                    """)
        
        st.markdown('### Report a bug, request a feature, or get in touch with me about anything:')

        contact_form = """
<form action="https://formsubmit.co/8be1eda9ec4663debabb07417ecc12dc" method="POST" enctype="multipart/form-data">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="text" name="_subject" placeholder="Subject">
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <input type="file" class="img_btn" name="Upload Image" accept="image/png, image/jpeg">
     <br>
     <input type="hidden" name="_next" value="https://dezoomcamp.streamlit.app/Thank%20you">
     <button type="submit">Send</button>
</form>
"""

        st.markdown(contact_form, unsafe_allow_html=True)


def contact_confirmation():
    st.toast('Feedback sent! Thank you!')