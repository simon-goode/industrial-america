import streamlit as st
import plotly.express as px
import pandas as pd

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

    Aenean iaculis in ante vitae imperdiet. Aenean scelerisque mi ac sem tempus, sed porttitor erat iaculis. Sed ut eleifend magna. Suspendisse orci quam, commodo sit amet ultrices vitae, laoreet in velit. Cras sed felis quam. Sed et dui mauris. Ut dignissim ipsum turpis, ut finibus augue ornare quis. Maecenas vulputate et felis eget posuere. Ut elementum, velit a egestas dictum, nisi mauris laoreet nibh, a elementum est nisi vehicula justo. Aliquam id suscipit ante. Cras dictum tristique mollis. Vivamus luctus at arcu in feugiat. Maecenas ultrices, massa eget tempor sollicitudin, sapien ante laoreet sapien, a gravida augue massa vestibulum tortor. Vivamus dapibus enim a fermentum malesuada. Proin maximus tortor ipsum, ac fringilla nibh vehicula rhoncus.

    Donec laoreet pulvinar dignissim. Pellentesque congue non augue sed faucibus. Nam sodales mi nec dolor ultricies gravida. Morbi vitae mi tincidunt, venenatis turpis ac, tristique urna. Cras faucibus faucibus mi vestibulum ullamcorper. Duis sagittis accumsan tellus eu vulputate. Praesent hendrerit ipsum quis lacus congue, a dictum nisl tristique. Aliquam scelerisque consequat ante ut fringilla. Nulla gravida ex sit amet nulla facilisis tincidunt.

    Quisque sed venenatis magna. Pellentesque et elementum augue. Ut malesuada at metus et lacinia. In hac habitasse platea dictumst. Sed semper odio sed mauris convallis, at imperdiet erat dapibus. Integer sollicitudin egestas venenatis. Donec dapibus, purus ac eleifend maximus, lectus nibh aliquam nisi, in ornare odio orci sit amet nisi. Donec quis diam scelerisque, aliquet nisi in, scelerisque libero.

    Curabitur suscipit sollicitudin turpis, at commodo sem consectetur sed. Praesent tristique tempus magna et lobortis. Nam vitae commodo ante, et feugiat erat. Vestibulum sed ipsum justo. Nulla sed metus sed odio faucibus rutrum. Mauris nec feugiat erat, eu condimentum eros. Curabitur vel pulvinar urna. Cras risus ante, rutrum quis aliquam eu, eleifend id purus. Suspendisse auctor congue lorem, sit amet faucibus lorem feugiat vitae. Integer aliquet justo ac massa scelerisque, vitae eleifend nunc fermentum. Nunc vehicula, tellus et sollicitudin ultrices, velit turpis interdum ante, in vulputate quam risus sed purus. Cras mollis ligula lorem, in posuere urna luctus varius. Aenean tempus magna dolor, nec ultrices lectus rhoncus sed.
            """)
        st.markdown('</div>', unsafe_allow_html=True)

    # about
    with tab6:
        st.markdown("""
            Heya, I'm Simon Goode, a student at Brandeis University studying Applied Math and Economics.
            
            [LinkedIn](https://www.linkedin.com/in/simon-goode-25581324a/)
            [GitHub](https://github.com/simon-goode/industrial-america)
                    """)