import streamlit as st
from modules.configcheck.config import ApplyChanges
from modules.json.json import LTjson
from modules.utils.lang import LANG
from modules.utils.sidebar import InitSidebar

InitSidebar()

sysjson = LTjson()

def AppyAndUpdate():
    ApplyChanges(
        st.session_state.fpslimit,
        st.session_state.lightingtech,
        st.session_state.oof,
        st.session_state.rpc,
        st.session_state.render,
        st.session_state.disablechat,
        st.session_state.fflagseditor,
        st.session_state.fontsize,
        st.session_state.useoldrobloxsounds
    )
    Currfflags = sysjson.ReadSoberConfig("fflags")
    st.session_state.fflagseditor = Currfflags

Currfflags = sysjson.ReadSoberConfig("fflags")
st.session_state.fflagseditor = Currfflags
st.button(
    LANG["lution.save.button.apply"],
    on_click=lambda : AppyAndUpdate(),
    key="apply_changes_button"
)
