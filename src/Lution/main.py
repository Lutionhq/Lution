# src/sostrapter/app.py
import streamlit as st
import os
from modules.utils.logging import log
from modules.json.json import LTjson
from modules.configcheck.config import LoadLightTechConfig, UsingOpenGl
from modules.utils.sidebar import InitSidebar

InitSidebar()

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")

log.info("Page : Home")





sysjson = LTjson()


st.html(
    """
    <style>
    div[aria-label="dialog"] > button[aria-label="Close"] {
        display: none;
    }
    div.stDialog backdrop-selector { pointer-events: none; }
    </style>
    """
)

# Set default values so they're always defined
if "fpslimit" not in st.session_state:
    log.info("Reading fpslimit")
    fpslimit = sysjson.ReadFflagsConfig("DFIntTaskSchedulerTargetFps")
if "lightingtech" not in st.session_state:
    log.info("Reading Lighting technology")
    tech = LoadLightTechConfig()
    st.session_state.lightingtech = tech
if "oof" not in st.session_state:
    oof = sysjson.ReadSoberConfig(key="bring_back_oof")
    st.session_state.oof = oof
if "rpc" not in st.session_state:
    log.info("Reading Discord RPC")
    drpc = sysjson.ReadSoberConfig("discord_rpc_enabled")
    st.session_state.rpc = drpc
if "render" not in st.session_state:
    log.info("Reading Render technology")
    st.session_state.render = UsingOpenGl()
if "disablechat" not in st.session_state:
    disablechat = sysjson.ReadFflagsConfig(flag_name="FFlagEnableBubbleChatFromChatService")
    st.session_state.disablechat = disablechat
if "customfont" not in st.session_state:
    log.info("Reading custom font")
    st.session_state.customfont = None
if "language" not in st.session_state:
    log.info("Reading language")
    st.session_state.language = "en"
if "fflagseditor" not in st.session_state:

    log.info("Reading FFlags editor")
    Currfflags = sysjson.ReadSoberConfig(key="fflags")
    st.session_state.fflagseditor = Currfflags
if "fontsize" not in st.session_state:
    log.info("Reading FFlag Fon size")
    st.session_state.fontsize = sysjson.ReadFflagsConfig(flag_name="FIntFontSizePadding")
if "useoldrobloxsounds" not in st.session_state:
    log.info("Reading Old roblox sounds")
    a = sysjson.ReadLutionConfig("OldRlbxSd")
    if a is None:
        a = False
    st.session_state.useoldrobloxsounds = a



Firstrun = sysjson.ReadLutionConfig("FirstRun")
if Firstrun == None :
    sysjson.UpdateLutionConfig("FirstRun",False)
    @st.dialog("What App you are using?")
    def dialog():
        st.write("Let us know you are usint Equinox or using sober")

        # pos the buttons
        left,right = st.columns(2)
        if left.button("I'am using Equinox",use_container_width=True) :
            sysjson.UpdateLutionConfig(key="Using",value="equinox")
            st.rerun()
            print(sysjson.robloxpath)
        if right.button("I'am using Sober",use_container_width=True) :
            sysjson.UpdateLutionConfig(key="Using", value="sober")
            st.rerun()
            print(sysjson.robloxpath)

    dialog()


st.write("This is home.")
if st.button("test"):
    sysjson.UpdateLutionConfig(key="FirstRun",value=None)
