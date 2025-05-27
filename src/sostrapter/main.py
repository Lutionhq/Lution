# src/sostrapter/app.py
import streamlit as st 
import os 
import json
from pathlib import Path
from modules.json.json import *
from modules.basic.messages import *
from modules.configcheck.config import *



aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")


try:
    with open(file_path, 'r') as f:
        sober_config = json.load(f)
except FileNotFoundError:
    st.sidebar.error(f"Error: The file '{file_path}' was not found.")
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    st.sidebar.error(f"Error: Could not decode JSON from the file '{file_path}'.")
    print(f"Error: Could not decode JSON from the file '{file_path}'.")
except Exception as e:
    st.sidebar.error(f"An unexpected error occurred: {e}")
    print(f"An unexpected error occurred: {e}")




if "page" not in st.session_state:
    st.session_state.page = "Mods"

if st.sidebar.button("Mods"):
    st.session_state.page = "Mods"
if st.sidebar.button("Appearance"):
    st.session_state.page = "Appearance"
if st.sidebar.button("Fast Flags"):
    st.session_state.page = "Fast Flags"
if st.sidebar.button("Apply Changes & Config"):
    st.session_state.page = "Apply Changes & Config"
if st.sidebar.button("About"):
    st.session_state.page = "About"

page = st.session_state.page

# Set default values so they're always defined
if "fpslimit" not in st.session_state:
    fpslimit = ReadFflagsConfig("DFIntTaskSchedulerTargetFps")
    st.session_state.fpslimit = fpslimit
if "lightingtech" not in st.session_state: # nah im lazy ass
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

if page == "Mods":
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

elif page == "Fast Flags":
    st.header("Fast Flags")
    st.session_state.oof = st.toggle("Bring back oof", value=st.session_state.oof)
    st.session_state.rpc = st.toggle("Enable Discord Rich Presence", value=st.session_state.rpc)
    st.session_state.fpslimit = st.text_input("FPS Limit", st.session_state.fpslimit, max_chars=3)
    st.session_state.render = st.selectbox(
        "Render Technology",
        ["OpenGL", "Vulkan"],
        index=0 if st.session_state.render else 1
    )
    st.session_state.lightingtech = st.selectbox(
        "Preferred Lighting Technology",
        ["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"],
        index=["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"].index(st.session_state.lightingtech)
    )

elif page == "Appearance":
    st.header("Appearance")

    st.markdown("""**Laucher Appearance Customization**""")
    st.markdown("""
    Maybe not possible,Sober itself is not very customizable, but you can wait to Vinegarhq-
    
    (Aka Sober team) to add a api to change the appearance of the launcher.
    """)

elif page == "About":
    st.markdown(aboutmd)

elif page == "Apply Changes & Config":
    st.download_button(
        label="Download Config",
        data=json.dumps({
            "fpslimit": st.session_state.fpslimit,
            "lightingtech": st.session_state.lightingtech
        }),
        file_name="config.json",
        mime="application/json"
    )
    data = st.file_uploader("Upload Config", type=["json"], key="config_uploader")
    st.button(
        "Apply Changes",
        on_click=apply_changes,
        args=(
            st.session_state.fpslimit,
            st.session_state.lightingtech,
            st.session_state.oof,
            st.session_state.rpc,
            st.session_state.render
        )
    )
