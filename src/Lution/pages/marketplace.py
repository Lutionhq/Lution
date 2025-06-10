import streamlit as st
import json
from modules.marketplace.downloadandinstall import DownloadMarketplace, ApplyMarketplace,RemoveMarketplace
from github import Github as g
from github.GithubException import UnknownObjectException
from modules.utils.lang import LANG
from modules.configcheck.config import UpdateLutionMarketplaceConfig as cfmk, ReadLutionMarketplaceConfig as rmk
from modules.utils.sidebar import InitSidebar

InitSidebar()
@st.cache_data(ttl=3600)  # Cache for 1 hour
def GetItemCached(repo_name, item):
    try :
        repo = g().get_repo(repo_name) 
        return repo.get_contents(item)
    except UnknownObjectException:
        return "Not found"

if "provider" not in st.session_state:
    cf = rmk("marketplaceprd")
    if cf == None:
        cfmk("marketplaceprd", "Lutionhq/Lution-Marketplace")
        st.session_state.prd = rmk("marketplaceprd")
    else : 
        st.session_state.prd = cf
    
if "theme" not in st.session_state:
    content_file = GetItemCached(st.session_state.prd, "Assets/Themes/content.json")
    if not content_file == "Not found":
        avdthemes = True
        st.session_state.theme = json.loads(content_file.decoded_content.decode())
    else :
        avdthemes = False
        st.error("NOT FOUND")
if "mod" not in st.session_state:
    content_file = GetItemCached(st.session_state.prd, "Assets/Mods/content.json")
    if not content_file == "Not found":
        avdmods = True
        st.session_state.mod = json.loads(content_file.decoded_content.decode())
    else :
        avdmods = False
        st.error("NOT FOUND")


def ChangeProvider(md):
    cfmk("marketplaceprd", md)

marketplace, installed,settings = st.tabs([LANG["lution.marketplace.tab.marketplace"], LANG["lution.marketplace.tab.installed"],LANG["lution.marketplace.tab.marketplacesettings"]])

global_index = 0

def create_columns(contents, content_type, cols_per_row=3):
    global global_index
    num_contents = len(contents)
    num_rows = (num_contents + cols_per_row - 1) // cols_per_row  

    for row_num in range(num_rows):
        cols = st.columns(cols_per_row, border=True)
        for col_idx in range(cols_per_row):
            content_index = row_num * cols_per_row + col_idx
            if content_index < num_contents:
                content = contents[content_index]
                with cols[col_idx]:
                    st.markdown(f"### {content.get('title', 'Untitled')}")
                    if "body" in content:
                        st.markdown(content.get("body", LANG["lution.marketplace.marketplace.nodescprovidered"]))
                    if "image" in content:
                        st.image(content.get("image"), use_container_width=True)
                    else:
                        st.image("https://placehold.co/600x400?text=No+Image", use_container_width=True)
                    if "version" in content :
                        st.caption(f"WINDOWSPLAYERVERSION: {content.get("version")}")
                    if "creator" in content:
                        st.markdown(f"**By:** {content.get('creator', 'Unknown')}")
                    if "sb" in content:
                        if content.get("sb") == "stable":
                            st.markdown(LANG["lution.marketplace.marketplace.badges.stable"], unsafe_allow_html=True)
                        elif content.get("sb") == "unstable":
                            st.markdown(LANG["lution.marketplace.marketplace.badges.unstable"], unsafe_allow_html=True)
                        else:
                            st.markdown(LANG["lution.marketplace.marketplace.badges.unkown"], unsafe_allow_html=True)
                    button_key = f"{content.get('title', 'Untitled')}_{global_index}"
                    if st.button(content.get("button", "Install"), key=button_key):
                        DownloadMarketplace(content.get("title", 'Untitled'), type=content_type)
                    global_index += 1

with marketplace:
    st.header(LANG["lution.marketplace.marketplace.title"])
    st.write(LANG["lution.marketplace.marketplace.decs"])
    st.markdown("""Docs about creating your own provider or add your own theme : [README.md](https://github.com/Lutionhq/Lution-Marketplace/blob/main/how-to/README.md)""")

    st.write(f"### {LANG["lution.marketplace.tab.themes"]}")
    if not avdthemes == False:
        if st.session_state.get("theme") is not None:
            with st.spinner(LANG["lution.marketplace.marketplace.spinner.download"]):
                create_columns(st.session_state.theme, "theme", cols_per_row=3)
    else: 
        st.write("Your provider does not have themes. Change your provider now.")

    st.write(f"### {LANG["lution.marketplace.tab.mods"]}")
    if not avdmods == False:
        if st.session_state.get("mod") is not None:
            with st.spinner(LANG["lution.marketplace.marketplace.spinner.download"]):
                create_columns(st.session_state.mod, "mod", cols_per_row=3)
    else :
        st.write("Your provider does not have mods. Change your provider now.")

with installed:
    st.header(LANG["lution.marketplace.installed.title"])
    st.write(LANG["lution.marketplace.title.decs"])
    theme = rmk("InstalledThemes")
    mod = rmk("InstalledMods")
    if theme:
        st.write(f"### {LANG["lution.marketplace.title.decs"]}")
        themes = theme.split(",")
        for t in themes:
            st.markdown(f"- {t}")
            if st.button(f"Apply {t}"):
                with st.spinner("Applying theme..."):
                    ApplyMarketplace(t, "theme")
            if st.button(f"Delete", key=f"deletebutton_{t}"):
                RemoveMarketplace(t, "theme")
                del st.session_state["theme"]
                st.rerun()

    if mod:
        st.write("### Mods")
        mods = mod.split(",")
        for m in mods:
            st.markdown(f"- {m}")
            if st.button(f"Apply {m}"):
                with st.spinner("Applying mod..."):
                    ApplyMarketplace(m, "mod")
            if st.button(f"Delete", key=f"deletebutton_{m}"):
                RemoveMarketplace(m, "mod")
                del st.session_state["mod"]
                st.rerun()
with settings:
    st.header("Markplace Settings")
    st.write("Here you can change your marketplace provider")
    st.session_state.pr = st.text_input("Marketplace Provider",st.session_state.prd, help="Change your marketplace provider. e.g Username/LutionMarketplace")
    st.button("Change Marketplace Provider", on_click=ChangeProvider(st.session_state.pr))