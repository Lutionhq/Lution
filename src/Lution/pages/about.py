import os
import streamlit as st
from modules.utils.logging import log
from modules.utils.sidebar import InitSidebar

InitSidebar()
log.info("Page : About")
aboutmd = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "markdown/about.md")).read()


st.markdown(aboutmd,unsafe_allow_html=True)
st.image("files/lutionhq.png")



st.image("files/lol/ballin-cat.png")
st.caption("look at this cat bro")