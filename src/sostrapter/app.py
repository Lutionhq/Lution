# src/sostrapter/app.py
import streamlit as st 
import os 
import json
from pathlib import Path

aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")

try:
    with open(file_path, 'r') as f:
        data = json.load(f)
    sober_config = json.dumps(data)
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


def success():
    """Display a success message."""
    st.susccess('', icon="✅")

def apply_changes(fpslimit, lightingtech):
    """Apply changes based on user input."""
    data = {
        "fpslimit": fpslimit,
        "lightingtech": lightingtech
    }
    print(json.dumps(data))

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
fpslimit = "60"
lightingtech = "potato"

if page == "Mods":
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

elif page == "Fast Flags":
    st.header("Fast Flags")
    oof = st.toggle("Bring back oof")
    rpc = st.toggle("Disable Discord Rich Presence")
    oldavatarbk = st.toggle("Use Old Avatar Background")    
    fpslimit = st.text_input("FPS Limit", fpslimit, max_chars=3)
    lightingtech = st.selectbox(
        "Preferred Lighting Technology",
        ["potato", "low", "test"],
        index=["potato", "low", "test"].index(lightingtech)
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
        data=json.dumps({"fpslimit": fpslimit, "lightingtech": lightingtech}),
        file_name="config.json",
        mime="application/json"
    )
    data = st.file_uploader("Upload Config", type=["json"], key="config_uploader")
    st.button("Apply Changes", on_click=apply_changes, args=(fpslimit, lightingtech))
