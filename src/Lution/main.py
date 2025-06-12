# src/sostrapter/app.py
import streamlit as st 
import os 
import json
from pathlib import Path
from modules.json.json import *
from modules.utils.messages import *
from modules.utils.files import *
from modules.configcheck.config import *
from modules.utils.lang import LANG , LANG_CODES, LANG_NAMES
from modules.utils.sidebar import InitSidebar

InitSidebar()

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")




try:
    with open(file_path, 'r') as f:
        sober_config = json.load(f)
except FileNotFoundError:
    st.sidebar.error(LANG[f"lution.message.error.filenotfound"])
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    st.sidebar.error(LANG[f"lution.message.error.jsondecode"])
    print(f"Error: Could not decode JSON from the file '{file_path}'.")
except Exception as e:
    st.sidebar.error(LANG["lution.message.error.unknown"])
    print(f"An unexpected error occurred: {e}")


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



# if "page" not in st.session_state:
#     st.session_state.page = "Mods"
# if st.sidebar.button(LANG["lution.tab.mods"]):
#     st.session_state.page = "Mods"
# if st.sidebar.button(LANG["lution.tab.appearance"]):
#     st.session_state.page = "Appearance"
# if st.sidebar.button(LANG["lution.tab.fflags"]):
#     st.session_state.page = "Fast Flags"
# if st.sidebar.button(LANG["lution.tab.apply"]):
#     st.session_state.page = "Apply Changes & Config"
# if st.sidebar.button(LANG["lution.tab.lutionsettings"]):
#     st.session_state.page = "Lution Settings"
# if st.sidebar.button(LANG["lution.tab.about"], key="about_button"):
#     st.session_state.page = "About"


# page = st.session_state.page

# Set default values so they're always defined
if "fpslimit" not in st.session_state:
    fpslimit = ReadFflagsConfig("DFIntTaskSchedulerTargetFps")
    st.session_state.fpslimit = fpslimit
if "lightingtech" not in st.session_state: 
    tech = LoadLightTechConfig()
    st.session_state.lightingtech = tech
if "oof" not in st.session_state:
    oof = ReadSoberConfig("bring_back_oof")
    st.session_state.oof = oof
if "rpc" not in st.session_state:
    drpc = ReadSoberConfig("discord_rpc_enabled")
    st.session_state.rpc = drpc
if "render" not in st.session_state:
    st.session_state.render = UsingOpenGl()
if "disablechat" not in st.session_state:
    disablechat = ReadFflagsConfig("FFlagEnableBubbleChatFromChatService")
    st.session_state.disablechat = disablechat
if "customfont" not in st.session_state:
    st.session_state.customfont = None
if "language" not in st.session_state:
    st.session_state.language = "en"
if "fflagseditor" not in st.session_state:
    Currfflags = ReadSoberConfig("fflags")
    st.session_state.fflagseditor = Currfflags
if "fontsize" not in st.session_state:
    st.session_state.fontsize = ReadFflagsConfig("FIntFontSizePadding")
if "useoldrobloxsounds" not in st.session_state:
    a = ReadLutionConfig("OldRlbxSd")
    if a is None:
        a = False  
    st.session_state.useoldrobloxsounds = a



Firstrun = ReadLutionConfig("FirstRun")
print(Firstrun)
if Firstrun == None :
    UpdateLutionConfig("FirstRun",False)
    @st.dialog("What App you are using?")
    def dialog():
        st.write("Let us know you are usint Equinox or using sober")

        # pos the buttons
        left,right = st.columns(2)
        if left.button("I'am using Equinox",use_container_width=True) :
            UpdateLutionConfig("Using","equinox")
            st.rerun()
        if right.button("I'am using Sober",use_container_width=True) :
            UpdateLutionConfig("Using", "sober")
            st.rerun()
        
    dialog()


st.write("This is home.")
if st.button("test"):
    UpdateLutionConfig("FirstRun",None)
    
