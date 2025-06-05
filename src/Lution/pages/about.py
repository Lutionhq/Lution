import os
import streamlit as st
from modules.utils.sidebar import InitSidebar

InitSidebar()
aboutmd = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "markdown/about.md")).read()


st.markdown(aboutmd,unsafe_allow_html=True)