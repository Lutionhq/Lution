import streamlit as st
import json
from modules.marketplace.downloadandinstall import DownloadMarketplace, ApplyMarketplace
from github import Github as g
from modules.configcheck.config import UpdateLutionMarketplaceConfig as cfmk, ReadLutionMarketplaceConfig as rmk
from modules.utils.sidebar import InitSidebar

InitSidebar()
@st.cache_data(ttl=3600)  # Cache for 1 hour
def GetItemCached(repo_name, item):
    repo = g().get_repo(repo_name)
    return repo.get_contents(item)

if st.session_state.get("theme") is None:
    content_file = GetItemCached("triisdang/Lution-Mods", "Assets/Themes/content.json")
    st.session_state.theme = json.loads(content_file.decoded_content.decode())
if st.session_state.get("mod") is None:
    content_file = GetItemCached("triisdang/Lution-Mods", "Assets/Mods/content.json")
    st.session_state.mod = json.loads(content_file.decoded_content.decode())

marketplace, installed = st.tabs(["Marketplace", "Installed"])

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
                        st.markdown(content.get("body", "No description provided."))
                    if "image" in content:
                        st.image(content.get("image"), use_container_width=True)
                    else:
                        st.image("https://placehold.co/600x400?text=No+Image", use_container_width=True)
                    if "creator" in content:
                        st.markdown(f"**By:** {content.get('creator', 'Unknown, Strapped by Lution dev')}")
                    if "sb" in content:
                        if content.get("sb") == "stable":
                            st.markdown('<span style="background-color: #4CAF50; color: white; padding: 2px 8px; border-radius: 8px;">✅ Stable</span>', unsafe_allow_html=True)
                        elif content.get("sb") == "unstable":
                            st.markdown('<span style="background-color: #f44336; color: white; padding: 2px 8px; border-radius: 8px;">⚠️ Unstable</span>', unsafe_allow_html=True)
                        else:
                            st.markdown('<span style="background-color: #9e9e9e; color: white; padding: 2px 8px; border-radius: 8px;">❓ Unknown</span>', unsafe_allow_html=True)
                    button_key = f"{content.get('title', 'Untitled')}_{global_index}"
                    if st.button(content.get("button", "Install"), key=button_key):
                        DownloadMarketplace(content.get("title", 'Untitled'), type=content_type)
                    global_index += 1

with marketplace:
    st.header("Marketplace")
    st.write("Welcome to the Lution Marketplace! Here you can find themes and mods to enhance your Roblox experience.")

    st.write("### Themes")
    if st.session_state.get("theme") is not None:
        with st.spinner("Downloading, Please be patient..."):
            create_columns(st.session_state.theme, "theme", cols_per_row=3)

    st.write("### Mods")
    if st.session_state.get("mod") is not None:
        with st.spinner("Downloading, Please be patient..."):
            create_columns(st.session_state.mod, "mod", cols_per_row=3)

with installed:
    st.header("Installed")
    st.write("Here you can see the themes and mods you have installed.")
    theme = rmk("InstalledThemes")
    mod = rmk("InstalledMods")
    if theme:
        st.write("### Themes")
        themes = theme.split(",")
        for t in themes:
            st.markdown(f"- {t}")
            if st.button(f"Apply {t}"):
                with st.spinner("Applying theme..."):
                    ApplyMarketplace(t, "theme")
    if mod:
        st.write("### Mods")
        mods = mod.split(",")
        for m in mods:
            st.markdown(f"- {m}")
            if st.button(f"Apply {m}"):
                with st.spinner("Applying mod..."):
                    ApplyMarketplace(m, "mod")