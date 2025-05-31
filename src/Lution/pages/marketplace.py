import streamlit as st
import json
from modules.marketplace.downloadandinstall import ApplyMarketplace
from github import Github as g
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


global_index = 0

def create_columns(contents, content_type):
    global global_index
    cols = st.columns(len(contents), border=True)
    for col, content in zip(cols, contents):
        with col:
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
                ApplyMarketplace(content.get("title", 'Untitled'), type=content_type)
        global_index += 1

st.header("Marketplace")
st.write("Welcome to the Lution Marketplace! Here you can find themes and mods to enhance your Sober experience.")

st.write("### Themes")
if st.session_state.get("theme") is not None:
    create_columns(st.session_state.theme, "theme")

st.write("### Mods")
if st.session_state.get("mod") is not None:
    create_columns(st.session_state.mods, "mod")