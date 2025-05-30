import streamlit as st 
import os 
import json
from pathlib import Path
from modules.utils.files import *
from modules.utils.lang import LANG


st.header(LANG["lution.tab.mods"])
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

FL = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/avatar/meshes")
st.button(
        LANG["lution.mods.button.openmesh"],
        on_click=OpenFolder,
        args=(FL,)
    )
st.caption(LANG["lution.mods.caption.littlenotice"])
st.button(
        LANG["lution.mods.button.resetmesh"],
        on_click=OverwriteFiles,
        args=(os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/avatar/meshes/"), [
            "files/mesh/leftarm.mesh",
            "files/mesh/rightarm.mesh",
            "files/mesh/leftleg.mesh",
            "files/mesh/rightleg.mesh",
            "files/mesh/torso.mesh"
        ])
    )