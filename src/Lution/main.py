# src/sostrapter/app.py
import streamlit as st 
import os 
import json
from pathlib import Path
from modules.json.json import *
from modules.basic.messages import *
from modules.configcheck.config import *
from modules.configcheck.fontreplacer import Replace
from modules.basic.mics import *




lutiontext = os.path.join(os.path.dirname(__file__), "files/lutiontext.svg")
with open(lutiontext, "r") as f:
    lutionlogo = f.read()


st.logo(lutionlogo, size="large")

st.sidebar.markdown("<h2>Lution</h2>", unsafe_allow_html=True)
st.sidebar.markdown(":orange-badge[⚠️ BETA]", unsafe_allow_html=True)
st.sidebar.caption("Version 0.1.0")

aboutmd = open(os.path.join(os.path.dirname(__file__), 'markdown/about.md')).read()


def OverwriteEmoji(dest_dir):
    src_file = os.path.join(os.path.dirname(__file__), 'files/RobloxEmoji.ttf')
    os.makedirs(dest_dir, exist_ok=True) 
    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
    shutil.copy2(src_file, dest_file)     


def applyfont():
    with st.spinner(LANG["lution.spinner.applyfont"]):
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

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
LANG_DIR = os.path.join(os.path.dirname(__file__), "files/languages")  
lang_files = [f for f in os.listdir(LANG_DIR) if f.endswith(".json")]
LANG_CODES = [os.path.splitext(f)[0] for f in lang_files]
LANG_NAMES = {
    "en": "English",
    "vn": "Tiếng Việt"
}

if "language" not in st.session_state:
    st.session_state.language = "en"

lang_choice = st.sidebar.selectbox(
    "Language",
    LANG_CODES,
    format_func=lambda code: LANG_NAMES.get(code, code),
    index=LANG_CODES.index(st.session_state.language)
)
st.session_state.language = lang_choice

lang_path = os.path.join(LANG_DIR, f"{st.session_state.language}.json")
with open(lang_path, "r") as f:
    LANG = json.load(f)

try:
    with open(file_path, 'r') as f:
        sober_config = json.load(f)
except FileNotFoundError:
    st.sidebar.error(LANG[f"lution.message.error.filenotfound"])
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    st.sidebar.error(LANG[f"lution.message.error.jsondecode"])
    print(f"Error: Could not decode JSON from the file '{file_path}'.")
except Exception as e:
    st.sidebar.error(LANG["lution.message.error.unknown"])
    print(f"An unexpected error occurred: {e}")



if "page" not in st.session_state:
    st.session_state.page = "Mods"
if st.sidebar.button(LANG["lution.tab.mods"]):
    st.session_state.page = "Mods"
if st.sidebar.button(LANG["lution.tab.appearance"]):
    st.session_state.page = "Appearance"
if st.sidebar.button(LANG["lution.tab.fflags"]):
    st.session_state.page = "Fast Flags"
if st.sidebar.button(LANG["lution.tab.apply"]):
    st.session_state.page = "Apply Changes & Config"
if st.sidebar.button("Lution Settings"):
    st.session_state.page = "Lution Settings"
if st.sidebar.button(LANG["lution.tab.about"]):
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
if "language" not in st.session_state:
    st.session_state.language = "en"






if page == "Mods":
    st.header(LANG["lution.tab.mods"])
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

elif page == "Fast Flags":
    FL = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/")
    st.header(LANG["lution.tab.fflags"])
    st.session_state.oof = st.toggle(LANG["lution.fflags.toggle.bringbackoof"], value=st.session_state.oof)
    st.session_state.rpc = st.toggle(LANG["lution.fflags.toggle.rpc"], value=st.session_state.rpc)
    st.session_state.disablechat = st.toggle(LANG["lution.fflags.toggle.bbchat"], value=st.session_state.disablechat)
    st.session_state.fpslimit = st.text_input(LANG["lution.fflags.textbox.fpslimit"], st.session_state.fpslimit, max_chars=3)
    st.session_state.render = st.selectbox(
        LANG["lution.fflags.mutichoices.render"],
        ["OpenGL", "Vulkan"],
        index=0 if st.session_state.render else 1
    )
    st.session_state.lightingtech = st.selectbox(
        LANG["lution.fflags.mutichoices.lighting"],
        ["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"],
        index=["Voxel Lighting (Phase 1)", "Shadowmap Lighting (Phase 2)", "Future Lighting (Phase 3)"].index(st.session_state.lightingtech)
    )
    st.write("Micsellaneous")
    st.button(
        "Open mesh avatar folder",
        on_click=open_folder(FL),)
    st.caption("Notice : Hey there gooners, i know what you are about to do, but PLEASEE for the love of god, DO NOT BREAK THE ROBLOX TOS.")


elif page == "Appearance":
    st.header("Appearance")
    st.session_state.customfont = st.file_uploader(
        LANG["lution.appearance.uploader.customfont"],
        type=["ttf", "otf"],
        key="custom_font_uploader"
    )
    st.button(
        LANG["lution.appearance.button.apply"],
        on_click=applyfont
    )
        
    st.header(LANG["lution.tab.appearance"])

    st.markdown(LANG["lution.appearance.text.laucher"])
    st.markdown("""
    Maybe not possible,Sober itself is not very customizable, but you can wait to Vinegarhq-
    
    (Aka Sober team) to add a api to change the appearance of the launcher.
    """)

elif page == "Lution Settings":
    st.markdown("""Should we add something? **Feature in the [isuess](https://github.com/triisdang/Lution/issues) page!**""")

elif page == "About":
    st.markdown(aboutmd)

elif page == "Apply Changes & Config":
    st.download_button(
        label=LANG["lution.save.button.downloadcf"],
        data=json.dumps({
            "fpslimit": st.session_state.fpslimit,
            "lightingtech": st.session_state.lightingtech
        }),
        file_name="config.json",
        mime="application/json"
    )
    data = st.file_uploader("Upload Config", type=["json"], key="config_uploader")
    st.button(
        LANG["lution.save.button.apply"],
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
