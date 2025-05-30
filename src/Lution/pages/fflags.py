import streamlit as st
import json
from modules.utils.lang import LANG
from modules.utils.files import OverlaySetup
from modules.configcheck.config import ReadSoberConfig
from modules.utils.sidebar import InitSidebar

InitSidebar()


st.header(LANG["lution.tab.fflags"])
st.session_state.oof = st.toggle(LANG["lution.fflags.toggle.bringbackoof"], value=st.session_state.oof)
st.session_state.rpc = st.toggle(LANG["lution.fflags.toggle.rpc"], value=st.session_state.rpc)
st.session_state.disablechat = st.toggle(LANG["lution.fflags.toggle.bbchat"], value=st.session_state.disablechat)
st.session_state.fpslimit = st.text_input(LANG["lution.fflags.textbox.fpslimit"], st.session_state.fpslimit, max_chars=3)
st.session_state.fontsize = st.text_input("Font size", value=st.session_state.fontsize, max_chars=2)
st.session_state.render = st.selectbox(
    LANG["lution.fflags.mutichoices.render"],
    ["OpenGL", "Vulkan"],
    index=0 if st.session_state.render else 1
)
st.session_state.lightingtech = st.selectbox(
    LANG["lution.fflags.mutichoices.lighting"],
    ["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"],
    index=["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"].index(st.session_state.lightingtech)
)
st.write(LANG["lution.fflags.text.advanded"])
st.button(
    LANG["lution.fflags.button.reseteditor"],
    on_click=lambda: st.session_state.update({"fflagseditor": ReadSoberConfig("fflags")})
)

# fflags editor
fflags_text = st.text_area(
    LANG["lution.fflags.texterea.fflagseditor"],
    value=json.dumps(st.session_state.fflagseditor, indent=4),
    height=300
)
try:
    parsed = json.loads(fflags_text)
    st.session_state.fflagseditor = parsed
except Exception:
    st.warning(LANG["lution.message.warning.fflags.invalid"])

st.write(LANG["lution.fflags.text.mics"])
st.button(
    LANG["lution.fflags.button.setupoverlay"],
    on_click=OverlaySetup
)
