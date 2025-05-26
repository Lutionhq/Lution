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

modstab , apprtab,ff, applychg, about, = st.tabs(["Mods", "Apppearance", "Fast Flags","Apply Changes & Config","About"])


# Mods Tab
with modstab:
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

# Fast Flags Tab
with ff:
    st.header("Fast Flags")
    fpslimit = st.text_input("FPS Limit","60",max_chars=3)
    lightingtech = st.selectbox(
        "Preferred Lighting Technology",
        ["potato", "low", "test"]
    )

# Appearance Tab
with apprtab:
    st.header("Appearance")
    st.write("This is the Appearance tab. You can customize the appearance here.")
    st.button("Change Appearance", on_click=success)

# About Tab
with about:
    st.markdown(aboutmd)

# Apply Changes & Config Tab
with applychg:
    st.download_button(
        label="Download Config",
        data=json.dumps({"fpslimit": fpslimit, "lightingtech": lightingtech}),
        file_name="config.json",
        mime="application/json"
    )
    data = st.file_uploader("Upload Config", type=["json"], key="config_uploader")
    
    st.button("Apply Changes", on_click=apply_changes, args=(fpslimit, lightingtech))