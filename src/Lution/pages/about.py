import os
import streamlit as st
aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()


st.markdown(aboutmd)