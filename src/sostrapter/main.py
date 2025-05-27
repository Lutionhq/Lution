# src/sostrapter/app.py
import streamlit as st 
import os 
import json
from pathlib import Path
from modules.json.json import *
from modules.basic.messages import *
from modules.configcheck.config import *
from modules.configcheck.fontreplacer import Replace




lutiontext = os.path.join(os.path.dirname(__file__), "files/lutiontext.svg")
with open(lutiontext, "r") as f:
    lutionlogo = f.read()


st.logo(lutionlogo, size="large")

st.sidebar.markdown("<h2>Lution</h2>", unsafe_allow_html=True)
st.sidebar.markdown(":orange-badge[⚠️ BETA]", unsafe_allow_html=True)
st.sidebar.caption("Version 0.1.0")

aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")

def OverwriteEmoji(dest_dir):
    src_file = os.path.join(os.path.dirname(__file__), 'files/RobloxEmoji.ttf')
    os.makedirs(dest_dir, exist_ok=True) 
    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
    shutil.copy2(src_file, dest_file)     


def applyfont():
    with st.spinner("Applying custom font..."):
        if st.session_state.customfont:
            # setup the overlay
            OverlaySetup()
            font_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/fonts")
            os.makedirs(font_dir, exist_ok=True)
            font_path = os.path.join(font_dir, st.session_state.customfont.name)
            with open(font_path, "wb") as f:
                f.write(st.session_state.customfont.getbuffer())
            Replace(
                font_path,
                os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/fonts")
            )
            try:
                os.remove(font_path)
            except Exception as e:
                st.warning(f"Could not delete temp font: {e}")
            OverwriteEmoji(os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/fonts"))
            st.success("Custom font applied successfully!")
        else:
            st.warning("No custom font uploaded.")


try:
    with open(file_path, 'r') as f:
        sober_config = json.load(f)
except FileNotFoundError:
    st.sidebar.error(f"Error: The file '{file_path}' was not found.")
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    st.sidebar.error(f"Error: Could not decode JSON from the file '{file_path}'.")
    print(f"Error: Could not decode JSON from the file '{file_path}'.")
except Exception as e:
    st.sidebar.error(f"An unexpected error occurred: {e}")
    print(f"An unexpected error occurred: {e}")



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
if "fpslimit" not in st.session_state:
    fpslimit = ReadFflagsConfig("DFIntTaskSchedulerTargetFps")
    st.session_state.fpslimit = fpslimit
if "lightingtech" not in st.session_state: 
    tech = LoadLightTechConfig()
    st.session_state.lightingtech = tech
if "oof" not in st.session_state:
    oof = ReadSoberConfig("bring_back_oof")
    st.session_state.oof = oof
if "rpc" not in st.session_state:
    drpc = ReadSoberConfig("discord_rpc_enabled")
    st.session_state.rpc = drpc
if "render" not in st.session_state:
    st.session_state.render = UsingOpenGl()
if "disablechat" not in st.session_state:
    disablechat = ReadFflagsConfig("FFlagEnableBubbleChatFromChatService")
    st.session_state.disablechat = disablechat
if "customfont" not in st.session_state:
    st.session_state.customfont = None

if page == "Mods":
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

elif page == "Fast Flags":
    st.header("Fast Flags")
    st.session_state.oof = st.toggle("Bring back oof", value=st.session_state.oof)
    st.session_state.rpc = st.toggle("Enable Discord Rich Presence", value=st.session_state.rpc)
    st.session_state.disablechat = st.toggle("Disable Chat", value=st.session_state.disablechat)
    st.session_state.fpslimit = st.text_input("FPS Limit", st.session_state.fpslimit, max_chars=3)
    st.session_state.render = st.selectbox(
        "Render Technology",
        ["OpenGL", "Vulkan"],
        index=0 if st.session_state.render else 1
    )
    st.session_state.lightingtech = st.selectbox(
        "Preferred Lighting Technology",
        ["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"],
        index=["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"].index(st.session_state.lightingtech)
    )

elif page == "Appearance":
    st.header("Appearance")
    st.session_state.customfont = st.file_uploader(
        "Upload Custom Font",
        type=["ttf", "otf"],
        key="custom_font_uploader"
    )
    st.button(
        "Apply Custom Font",
        on_click=applyfont
    )
        
    st.markdown("""**Laucher Appearance Customization**""")
    st.markdown("""
    Maybe not possible,Sober itself is not very customizable, but you can wait to Vinegarhq-
    
    (Aka Sober team) to add a api to change the appearance of the launcher.
    """)

elif page == "About":
    st.markdown(aboutmd)

elif page == "Apply Changes & Config":
    st.download_button(
        label="Download Config",
        data=json.dumps({
            "fpslimit": st.session_state.fpslimit,
            "lightingtech": st.session_state.lightingtech
        }),
        file_name="config.json",
        mime="application/json"
    )
    data = st.file_uploader("Upload Config", type=["json"], key="config_uploader")
    st.button(
        "Apply Changes",
        on_click=apply_changes,
        args=(
            st.session_state.fpslimit,
            st.session_state.lightingtech,
            st.session_state.oof,
            st.session_state.rpc,
            st.session_state.render,
            st.session_state.disablechat,
            st.session_state.customfont if st.session_state.customfont else None
        )
    )
