import streamlit as st
import plotly.express as px
import pandas as pd
from scripts.parse_chart1 import *

st.set_page_config(page_title='American Industry Project', layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("src/style/style.css")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.link_button("Support American Labor", url="https://aflcio.org/relief")
    st.link_button("Pro-Union Scorecards", url="https://aflcio.org/scorecard")
    st.link_button("Made in USA Directory", url="https://www.americanmanufacturing.org/made-in-america/")

with col2:
    st.markdown('<div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Overview", "Dismantled", "Michigan", "Ohio", "Pennsylvania", "Wisconsin", "About"])

    # overview
    with tab1:

        # st.image("src/visuals/rustbelt.png", width=750)
        st.markdown('## Rust Belt Revolution')

        # vote margin differential from previous election, by county
        year = st.slider("Year:", 2004, 2020, step=4)
        chart1_tab1, chart1_tab2 = st.tabs(["Presidential Vote Margin", "Change in Presidential Vote Margin"])
        with chart1_tab1:
            st.plotly_chart(get_vote_margin(year))
            st.markdown(f"""
                    How much do swing counties swing? This map shows how blue or red each county of the Rust Belt :blue[voted in the {year} U.S.] election.
        """)
        with chart1_tab2:
            # st.image(f"src/visuals/chart1/{year}.png", use_column_width=True)
            st.plotly_chart(get_vote_margin_diff(year))
            st.markdown("""
                    How much do swing counties swing? This map shows how blue or red each county of the Rust Belt :red[shifted from the prior] election.
        """)
        #graph blurb    
        st.warning('Play around with the slider. What swing do you see for Obama/McCain in 2008? For Obama/Romney? For Trump/Clinton in 2016?')
        # paragraph 1
        st.markdown('''These maps starkly highlight the growing urban-rural divide in America: the ruby red counties are numerous sparse expanses,
                    while the bluest counties are few and separated, in ultra-dense urban hubs. But this division can't explain everything; namely, what happened in 2016.
                    While Hillary Clinton largely underperformed Barack Obama nationwide, she fell particularly flat in these critical Rust Belt swing states. Trump
                    seemed to capture the loyalty of Midwestern whites, especially with the traditionally progressive demographic of industrial working class men.
                    Despite this, volumes of research<sup>[\[1\]](https://www.institutmontaigne.org/en/expressions/trump-symptom-diseased-american-democracy)
                    [\[2\]](https://smallwarsjournal.com/jrnl/art/problematic-symptom-donald-j-trump)</sup>and commentary<sup>
                    [\[3\]](https://www.carnegiecouncil.org/media/article/trump-is-the-symptom-not-the-problem)
                    [\[4\]](https://www.thetimes.com/world/us-world/article/is-trump-a-symptom-or-the-cause-of-the-us-s-bitterpolitical-divide-ghrb9pz2b)
                    [\[5\]](https://www.bostonglobe.com/2021/01/10/opinion/trump-is-symptom-our-moral-decline-not-cause/)</sup>
                    since 2016 point to Donald Trump being a symptom, more than the cause, of the growing division and recent populist slant in United States politics. 
                    So if it *wasn't* Trump riding down the escalator in 2016 that changed everything, the question is obvious:<br>''', unsafe_allow_html=True)
        st.markdown('''### Why here? And why now?''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    #michigan
    with tab3:
        st.image("src/visuals/watercolor/michigan.png", width=400)
    #ohio
    with tab4:
        st.image("src/visuals/watercolor/ohio.png", width=400)
    #pennsylvania
    with tab5:
        st.image("src/visuals/watercolor/pennsylvania.png", width=400)
    #wisconsin
    with tab6:
        st.image("src/visuals/watercolor/wisconsin.png", width=400)
    # about
    with tab7:
        st.markdown("""
            Hi there, I'm Simon Goode, a student at Brandeis University studying Applied Math and Economics.
            
            [LinkedIn](https://www.linkedin.com/in/simon-goode-25581324a/)     [GitHub](https://github.com/simon-goode/industrial-america)
                    """)
        
        st.markdown('### Report a bug, fact check me, or just get in touch!:')

        contact_form = """
<form action="https://formsubmit.co/8be1eda9ec4663debabb07417ecc12dc" method="POST" enctype="multipart/form-data">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="text" name="_subject" placeholder="Subject">
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <input type="file" class="img_btn" name="Upload Image" accept="image/png, image/jpeg">
     <br>
     <input type="hidden" name="_next" value="americanindustryproject.streamlit.app">
     <button type="submit">Send</button>
</form>
"""

        st.markdown(contact_form, unsafe_allow_html=True)


def contact_confirmation():
    st.toast('Feedback sent! Thank you!')