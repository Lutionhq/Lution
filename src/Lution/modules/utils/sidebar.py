import streamlit as st
from modules.utils.lang import LANG
import os


def InitSidebar():
    lutiontext = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "files", "lutiontext.svg")
    with open(lutiontext, "r") as f:
        lutionlogo = f.read()

    st.logo(lutionlogo, size="large")

    st.sidebar.markdown("<h2>Lution</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(":orange-badge[⚠️ BETA]")
    st.sidebar.caption("Version 0.2.0")

    st.sidebar.page_link("pages/appearance.py", label=LANG["lution.tab.appearance"], icon="🛠️")
    st.sidebar.page_link("pages/about.py", label=LANG["lution.tab.about"], icon="ℹ️")
    st.sidebar.page_link("pages/fflags.py", label=LANG["lution.tab.fflags"], icon="⚡")
    st.sidebar.page_link("pages/mods.py", label=LANG["lution.tab.mods"], icon="🧩")
    st.sidebar.page_link("pages/apply.py", label=LANG["lution.tab.apply"], icon="✅")
    st.sidebar.page_link("pages/lutionsettings.py", label=LANG["lution.tab.lutionsettings"], icon="⚙️")