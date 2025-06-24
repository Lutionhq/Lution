# src/Lution/app.py
import streamlit as st 
import os 
import json
from modules.utils.logging import log
from modules.json.json import *
from modules.utils.messages import *
from modules.utils.files import *
from modules.configcheck.config import *
from modules.utils.lang import LANG , LANG_CODES, LANG_NAMES
from modules.utils.sidebar import InitSidebar

InitSidebar()

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")

log.info("Page : Home")



# Set default values so they're always defined
if "fpslimit" not in st.session_state:
    log.info("Reading fpslimit")
    fpslimit = ReadFflagsConfig("DFIntTaskSchedulerTargetFps")
    st.session_state.fpslimit = fpslimit
if "lightingtech" not in st.session_state: 
    log.info("Reading Lighting technology")
    tech = LoadLightTechConfig()
    st.session_state.lightingtech = tech
if "texturequality" not in st.session_state: 
    log.info("Reading Texture Quality")
    qua = LoadTextureQuality()
    st.session_state.texturequality = qua
if "mssa" not in st.session_state: 
    log.info("Reading msaa")
    msaa = LoadMSAA()
    st.session_state.msaa = msaa
if "oof" not in st.session_state:
    log.info("Reading Oof")
    oof = ReadSoberConfig("bring_back_oof")
    st.session_state.oof = oof
if "rpc" not in st.session_state:
    log.info("Reading Discord RPC")
    drpc = ReadSoberConfig("discord_rpc_enabled")
    st.session_state.rpc = drpc
if "render" not in st.session_state:
    log.info("Reading Render technology")
    st.session_state.render = UsingOpenGl()
if "disablechat" not in st.session_state:
    log.info("Reading FFlag Disnable chat service")
    disablechat = ReadFflagsConfig("FFlagEnableBubbleChatFromChatService")
    st.session_state.disablechat = disablechat
if "customfont" not in st.session_state:
    log.info("Reading custom font")
    st.session_state.customfont = None
if "language" not in st.session_state:
    log.info("Reading language")
    st.session_state.language = "en"
if "fflagseditor" not in st.session_state:
    log.info("Reading FFlags editor")
    Currfflags = ReadSoberConfig("fflags")
    st.session_state.fflagseditor = Currfflags
if "fontsize" not in st.session_state:
    log.info("Reading FFlag Fon size")
    st.session_state.fontsize = ReadFflagsConfig("FIntFontSizePadding")
if "disableplayersh" not in st.session_state:
    log.info("Reading Disnable player shadows")
    dis = ReadLutionConfig("disableplayersh")
    if dis == None :
        st.session_state.disableplayersh = False
    else:
        st.session_state.disableplayersh = dis
if "useoldrobloxsounds" not in st.session_state:
    log.info("Reading Old roblox sounds")
    a = ReadLutionConfig("OldRlbxSd")
    if a is None:
        a = False  
    st.session_state.useoldrobloxsounds = a



st.header("Wellcome to Lution!")
st.image("files/cooked.png")
st.write("Lution is a boostrapper for sober, try out one of the feature!")
st.write("Thank you for using Lution!")
st.write("-- Lution dev team")