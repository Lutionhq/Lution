import streamlit as st
from modules.utils.lang import LANG
from modules.utils.logging import log
from modules.configcheck.VERSION import GIT_COMMIT, COMMIT_DATE
import os


def InitSidebar():
    lutiontext = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "files", "lutiontext.svg")
    # with open(lutiontext, "r") as f:
    #     lutionlogo = f.read()

    # st.logo(lutionlogo, size="large")
    st.sidebar.image(lutiontext, width=200) # Adjust width as needed
    st.logo(image="files/lution1.svg",icon_image="files/lution1.svg")
    st.sidebar.markdown("<h2>Lution</h2>", unsafe_allow_html=True)
    st.sidebar.badge("Stable", icon=":material/check:", color="green")
    st.sidebar.caption("Version 0.2.6")

    st.sidebar.page_link("main.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/marketplace.py", label=LANG["lution.tab.marketplace"], icon="🛒")
    st.sidebar.page_link("pages/mods.py", label=LANG["lution.tab.mods"], icon="🧩")
    st.sidebar.page_link("pages/appearance.py", label=LANG["lution.tab.appearance"], icon="🛠️")
    st.sidebar.page_link("pages/fflags.py", label=LANG["lution.tab.fflags"], icon="⚡")
    st.sidebar.page_link("pages/apply.py", label=LANG["lution.tab.apply"], icon="✅")
    st.sidebar.page_link("pages/lutionsettings.py", label=LANG["lution.tab.lutionsettings"], icon="⚙️")
    st.sidebar.page_link("pages/about.py", label=LANG["lution.tab.about"], icon="ℹ️")
    st.sidebar.container()
    st.sidebar.caption(f"Running commit : {GIT_COMMIT[:7]}")
    log.info("Success init sidebar")
