
import streamlit as st
from modules.utils.files import ApplyFont
from modules.utils.lang import LANG
from modules.configcheck.config import UpdateCursor



st.header(LANG["lution.tab.appearance"])
    

st.session_state.customfont = st.file_uploader(
    LANG["lution.appearance.uploader.customfont"],
    type=["ttf", "otf"],
    key="custom_font_uploader"
)
st.button(
    LANG["lution.appearance.button.applyfont"],
    on_click=ApplyFont
    )
st.session_state.cursor = st.selectbox(
        LANG["lution.appearance.mutichoices.cursor"],
        ["Default", "Old 2007 Cursor", "Old 2013 Cursor"],
        index=["Default", "Old 2007 Cursor", "Old 2013 Cursor"].index(st.session_state.cursor)
    )
st.button(
        LANG["lution.appearance.button.applycursor"],
        on_click=lambda: UpdateCursor(st.session_state.cursor),
        key="apply_cursor_button"
    )


        

st.markdown(LANG["lution.appearance.text.laucher"])
st.markdown("""
Maybe not possible,Sober itself is not very customizable, but you can wait to Vinegarhq-
    
(Aka Sober team) to add a api to change the appearance of the launcher.
""")