import streamlit as st
from github import Github as g
import json
from modules.utils.sidebar import InitSidebar

InitSidebar()
@st.cache_data(ttl=3600)  # Cache for 1 hour
def GetItemCached(repo_name, item):
    repo = g().get_repo(repo_name)
    return repo.get_contents(item)

if st.session_state.get("theme") is None:
    content_file = GetItemCached("triisdang/Lution-Mods", "Assets/Themes/content.json")
    st.session_state.theme = json.loads(content_file.decoded_content.decode())
if st.session_state.get("mods") is None:
    content_file = GetItemCached("triisdang/Lution-Mods", "Assets/Mods/content.json")
    st.session_state.mods = json.loads(content_file.decoded_content.decode())

def check(name):
    st.write(name)

global_index = 0

def create_columns(contents):
    global global_index
    cols = st.columns(len(contents), border=True)
    for idx, (col, content) in enumerate(zip(cols, contents)):
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

            button_key = f"{content.get('title', 'Untitled')}_{global_index}"
            if st.button(content.get("button", "Install"), key=button_key):
                check(content.get("title", 'Untitled'))
        global_index += 1

st.header("Marketplace")
st.write("Welcome to the Lution Marketplace! Here you can find themes and mods to enhance your Sober experience.")

st.write("### Themes")
if st.session_state.get("theme") is not None:
    create_columns(st.session_state.theme)

st.write("### Mods")
if st.session_state.get("mods") is not None:
    create_columns(st.session_state.mods)