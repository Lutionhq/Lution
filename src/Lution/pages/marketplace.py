import streamlit as st
import json
from modules.marketplace.downloadandinstall import DownloadMarketplace, ApplyMarketplace, RemoveMarketplace
from github import Github as g
from github.GithubException import UnknownObjectException
from modules.utils.lang import LANG
from modules.utils.logging import log
from modules.configcheck.config import UpdateLutionMarketplaceConfig as cfmk, ReadLutionMarketplaceConfig as rmk
from modules.utils.sidebar import InitSidebar

InitSidebar()
log.info("Page : Marketplace")


@st.cache_data(ttl=3600)
def GetItemCached(repo_name, item):
    try:
        repo = g().get_repo(repo_name)
        return repo.get_contents(item)
    except UnknownObjectException:
        return "Not found"

if "provider" not in st.session_state:
    cf = rmk("marketplaceprd")
    if cf is None:
        cfmk("marketplaceprd", "Lutionhq/Lution-Marketplace")
        st.session_state.prd = rmk("marketplaceprd")
    else:
        st.session_state.prd = cf

def loadbar():
    progress = st.progress(0)
    progress.progress(10)

    avdmods = GetItemCached(st.session_state.prd, "Assets/Mods/content.json") != "Not found"
    progress.progress(30)

    avdthemes = GetItemCached(st.session_state.prd, "Assets/Themes/content.json") != "Not found"
    progress.progress(50)

    def loadcontent(key, path, prog_value):
        if key not in st.session_state:
            content_file = GetItemCached(st.session_state.prd, path)
            if content_file != "Not found":
                st.session_state[key] = json.loads(content_file.decoded_content.decode())
            else:
                st.error(f"{key.upper()} NOT FOUND")
        progress.progress(prog_value)

    loadcontent("theme", "Assets/Themes/content.json", 75)
    loadcontent("mod", "Assets/Mods/content.json", 100)

    progress.empty()
    return avdmods, avdthemes



avdmods, avdthemes = loadbar()


def ChangeProvider():
    new_provider = st.session_state.get("pr")
    if new_provider:
        cfmk("marketplaceprd", new_provider)
        log.warn(f"Changed marketplace provider to: {new_provider}")

marketplace, installed, settings = st.tabs([
    LANG["lution.marketplace.tab.marketplace"],
    LANG["lution.marketplace.tab.installed"],
    LANG["lution.marketplace.tab.marketplacesettings"]
])

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
                    st.markdown(content.get("body", LANG["lution.marketplace.marketplace.nodescprovidered"]))
                    st.image(content.get("image", "https://placehold.co/600x400?text=No+Image"), use_container_width=True)
                    if "version" in content:
                        st.caption(f"WINDOWSPLAYERVERSION: {content.get('version')}")
                    if "creator" in content:
                        st.markdown(f"**By:** {content.get('creator', 'Unknown')}")
                    sb = content.get("sb")
                    if sb == "stable":
                        st.markdown(LANG["lution.marketplace.marketplace.badges.stable"], unsafe_allow_html=True)
                    elif sb == "unstable":
                        st.markdown(LANG["lution.marketplace.marketplace.badges.unstable"], unsafe_allow_html=True)
                    else:
                        st.markdown(LANG["lution.marketplace.marketplace.badges.unkown"], unsafe_allow_html=True)
                    button_key = f"{content.get('title', 'Untitled')}_{global_index}"
                    if st.button(content.get("button", "Install"), key=button_key):
                        log.info(f"Installing {content.get('title', 'Untitled')}")
                        DownloadMarketplace(content.get("title", 'Untitled'), type=content_type)
                    global_index += 1

with marketplace:
    st.header(LANG["lution.marketplace.marketplace.title"])
    st.write(LANG["lution.marketplace.marketplace.decs"])
    st.markdown("[README.md](https://github.com/Lutionhq/Lution-Marketplace/blob/main/how-to/README.md)")

    #st.write(f"### {LANG['lution.marketplace.tab.themes']}")
    if avdthemes and st.session_state.get("theme"):
        with st.spinner(LANG["lution.marketplace.marketplace.spinner.download"]):
            log.info("Creating Themes col")
            themeexpander = st.expander(LANG['lution.marketplace.tab.themes'])
            with themeexpander:
                create_columns(st.session_state.theme, "theme", cols_per_row=3)
    else:
        st.write("Your provider does not have themes. Change your provider now.")

    #st.write(f"### {LANG['lution.marketplace.tab.mods']}")
    if avdmods and st.session_state.get("mod"):
        with st.spinner(LANG["lution.marketplace.marketplace.spinner.download"]):
            log.info("Creating Mods col")
            modsexpander = st.expander(LANG['lution.marketplace.tab.mods'])
            with modsexpander:
                create_columns(st.session_state.mod, "mod")
    else:
        st.write("Your provider does not have mods. Change your provider now.")

with installed:
    st.header(LANG["lution.marketplace.installed.title"])
    st.write(LANG["lution.marketplace.title.decs"])
    theme = rmk("InstalledThemes")
    mod = rmk("InstalledMods")
    st.write(f"### {LANG['lution.marketplace.title.decs']}")
    if theme:
        themesexpander = st.expander("Themes", expanded=True)
        with themesexpander:
            for t in theme.split(","):
                colleft1, colmid1,colright1 = st.columns(3)
                with colleft1:
                    st.markdown(f"- {t}")
                with colmid1:
                    if st.button(f"Apply {t}", use_container_width=True):
                        with st.spinner("Applying theme..."):
                            log.info(f"Applying {t}")
                            ApplyMarketplace(t, "theme")
                with colright1:
                    if st.button(f"Delete", key=f"deletebutton_{t}",use_container_width=True):
                        log.info(f"Deleted {t}")
                        RemoveMarketplace(t, "theme")
                        del st.session_state["theme"]
                        st.rerun()

    if mod:
        modsexpander = st.expander("Mods", expanded=True)
        with modsexpander:
            for m in mod.split(","):
                colleft2, colmid2, colright2 = st.columns(3)
                with colleft2:
                    st.markdown(f"- {m}")
                with colmid2:
                    if st.button(f"Apply {m}", use_container_width=True):
                        with st.spinner("Applying mod..."):
                            log.info(f"Applying {m}")
                            ApplyMarketplace(m, "mod")
                with colright2:
                    if st.button(f"Delete", key=f"deletebutton_{m}", use_container_width=True):
                        log.info(f"Deleted {m}")
                        RemoveMarketplace(m, "mod")
                        del st.session_state["mod"]
                        st.rerun()

with settings:
    st.header("Marketplace Settings")
    st.write("Here you can change your marketplace provider")
    st.text_input("Marketplace Provider", value=st.session_state.prd, key="pr", help="e.g Username/LutionMarketplace")
    st.button("Change Marketplace Provider", on_click=lambda : ChangeProvider() )
