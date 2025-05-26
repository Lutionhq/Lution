# src/sostrapter/app.py
import streamlit as st 
import os 
import json

aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()

def success():
    """Display a success message."""
    st.success('', icon="✅")

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