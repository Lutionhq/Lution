# src/sostrapter/app.py
import streamlit as st 
import os 

aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()

def success():
    """Display a success message."""
    st.success('', icon="✅")
    
modstab , apprtab, about,ff = st.tabs(["Mods", "Apppearance","About", "Fast Flags"])

with modstab:
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)
with ff:
    st.header("Fast Flags")
    st.text_input("FPS Limit","60")

with apprtab:
    st.header("Appearance")
    st.write("This is the Appearance tab. You can customize the appearance here.")
    st.button("Change Appearance", on_click=success)
with about:
    st.markdown(aboutmd)

