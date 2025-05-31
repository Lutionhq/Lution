import streamlit as st 
import os 
from modules.utils.files import *
from modules.utils.lang import LANG
from modules.utils.sidebar import InitSidebar

InitSidebar()

st.header(LANG["lution.tab.mods"])
st.session_state.useoldrobloxsounds = st.toggle("Use old roblox sounds", value=st.session_state.useoldrobloxsounds, key="toogle old roblox sounds")

mods = os.path.expanduser("~/Documents/Lution/Mods")
st.button(
    "Open Mods Folder",
    on_click=lambda : ModsFolder(), 
    key = "mod_button"
)
st.caption("By the way, we support bloxstrap mods :) (most of it, if your mod does not work, go to the issues page on github)")
st.button(
    "Apply Mods",
    on_click=lambda: ApplyMods(),
    key="apply_mods_button"

)

st.button(
        "Reset Roblox to default",
        on_click=lambda: ResetMods(),
        key="reset_mods_button"
    )

# yay