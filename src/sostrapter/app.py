# src/sostrapter/app.py
import streamlit as st 
import os 
import json
from pathlib import Path

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

def update_fflag(flag_name, flag_value):
    try:
        if "fflags" not in sober_config or not isinstance(sober_config["fflags"], dict):
            sober_config["fflags"] = {}
        sober_config["fflags"][flag_name] = flag_value
        with open(file_path, "w") as f:
            json.dump(sober_config, f, indent=4)
        st.success(f"fflags['{flag_name}'] set to {flag_value}")
    except Exception as e:
        st.error(f"Failed to update fflags: {e}")
def UpdateSoberConfig(key, value):
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        config[key] = value
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
        st.success(f"Config['{key}'] set to {value}")
    except Exception as e:
        st.error(f"Failed to update config: {e}")
        
def success():
    """Display a success message."""
    st.susccess('', icon="✅")

def apply_changes(fpslimit, lightingtech, oof1, rpc1):
    """Apply changes based on user input."""
    # Lighting Tech
    if lightingtech == "Voxel Lighting (Phase 1)" : 
        update_fflag("DFFlagDebugRenderForceTechnologyVoxel",True)
    if lightingtech == "Shadowmap Lighting (Phase 2)" :
        update_fflag("FFlagDebugForceFutureIsBrightPhase2",True)
    if lightingtech == "Future Lighting (Phase 3)" :
        update_fflag("FFlagDebugForceFutureIsBrightPhase3",True)
    # FPS limit
    update_fflag("DFIntTaskSchedulerTargetFps",fpslimit)
    update_fflag("FFlagGameBasicSettingsFramerateCap5",False)
    update_fflag("FFlagTaskSchedulerLimitTargetFpsTo2402",False)
    #Bringbackoof - ts is a hashtag lol 🥀
    UpdateSoberConfig("bring_back_oof",oof1)
    # Disnabel Discord RPC
    UpdateSoberConfig("discord_rpc_enabled",rpc1)



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
    st.session_state.fpslimit = "60"
if "lightingtech" not in st.session_state:
    st.session_state.lightingtech = "Voxel Lighting (Phase 1)"
if "oof" not in st.session_state:
    st.session_state.oof = False
if "rpc" not in st.session_state:
    st.session_state.rpc = False

if page == "Mods":
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

elif page == "Fast Flags":
    st.header("Fast Flags")
    st.session_state.oof = st.toggle("Bring back oof", value=st.session_state.oof)
    st.session_state.rpc = st.toggle("Disable Discord Rich Presence", value=st.session_state.rpc)
    st.session_state.fpslimit = st.text_input("FPS Limit", st.session_state.fpslimit, max_chars=3)
    st.session_state.lightingtech = st.selectbox(
        "Preferred Lighting Technology",
        ["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"],
        index=["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"].index(st.session_state.lightingtech)
    )

elif page == "Appearance":
    st.header("Appearance")
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
            st.session_state.rpc
        )
    )
