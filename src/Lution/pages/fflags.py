import streamlit as st
import json
from modules.utils.lang import LANG
from modules.utils.logging import log
from modules.utils.files import OverlaySetup
from modules.configcheck.config import ReadSoberConfig
from modules.configcheck.config import Applyfflags
from modules.utils.sidebar import InitSidebar

InitSidebar()

log.info("Page : Fflags")

st.header(LANG["lution.tab.fflags"])
st.session_state.oof = st.toggle(LANG["lution.fflags.toggle.bringbackoof"], value=st.session_state.oof)
st.session_state.rpc = st.toggle(LANG["lution.fflags.toggle.rpc"], value=st.session_state.rpc)
st.session_state.fpslimit = st.text_input(LANG["lution.fflags.textbox.fpslimit"], st.session_state.fpslimit, max_chars=3)
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
# fflags presets
st.write("fflags presets")
st.session_state.disablechat = st.toggle(LANG["lution.fflags.toggle.bbchat"], value=st.session_state.disablechat)
st.session_state.fontsize = st.text_input(LANG["lution.appearance.textbox.fontsize"], value=st.session_state.fontsize, max_chars=2)
st.toggle("Disable player shadows", value=st.session_state.disableplayersh)
st.session_state.texturequality = st.selectbox(
    "Texture quality",
    ["Off","Level 0 (potato)", "Level 1 (Low)","Level 2 (Medium)","Level 3 (High)","Level 4 (Ultra)"],
    index=["Off","Level 0 (potato)", "Level 1 (Low)","Level 2 (Medium)","Level 3 (High)","Level 4 (Ultra)"].index(st.session_state.texturequality)
)

# advanded
st.write(LANG["lution.fflags.text.advanded"])
st.button(
    LANG["lution.fflags.button.reseteditor"],
    on_click=lambda: st.session_state.update({"fflagseditor": ReadSoberConfig("fflags")})
)

# fflags editor
if "fflags_text" not in st.session_state:
    st.session_state.fflags_text = json.dumps(st.session_state.fflagseditor, indent=4)

fflags_text = st.text_area(
    LANG["lution.fflags.texterea.fflagseditor"],
    value=st.session_state.fflags_text,
    height=300
)

try:
    parsed = json.loads(fflags_text)
    st.session_state.fflagseditor = parsed
    print(st.session_state.fflagseditor)
except Exception:
    log.warn("Invalid fflags config")
    st.warning(LANG["lution.message.warning.fflags.invalid"])

lf, mid ,rgt = st.columns(3)
st.caption("The fflags editor slow to update with the config, recommend restart lution then try again")
with mid:
    st.button(
        "Apply FFlags",
        on_click=lambda : Applyfflags(st.session_state.fflagseditor),
        use_container_width=True
    )

st.write(LANG["lution.fflags.text.mics"])
st.button(
    LANG["lution.fflags.button.setupoverlay"],
    on_click=OverlaySetup
)
