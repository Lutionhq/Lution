import os
import shutil
import json
import subprocess
import platform
import streamlit as st
from .messages import success , warning as warn
from modules.utils.lang import LANG
from modules.configcheck.fontreplacer import Replace


def OverwriteFiles(dest_dir, src_files):
    os.makedirs(dest_dir, exist_ok=True)

    for src_path in src_files:
        if not os.path.isabs(src_path):
            raise ValueError(f"Expected absolute path, got: {src_path}")

        if not os.path.isfile(src_path):
            raise FileNotFoundError(f"Source file does not exist: {src_path}")

        filename = os.path.basename(src_path)
        dest_path = os.path.join(dest_dir, filename)

        shutil.copy2(src_path, dest_path)
    success()

def OverwriteFolders(dest_dir, src_dirs, no_success=False):

    os.makedirs(dest_dir, exist_ok=True)

    for src_path in src_dirs:
        if not os.path.isabs(src_path):
            raise ValueError(f"Expected absolute path, got: {src_path}")

        if not os.path.isdir(src_path):
            continue  # Skip if not a directory

        folder_name = os.path.basename(os.path.normpath(src_path))
        dest_path = os.path.join(dest_dir, folder_name)

        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        shutil.copytree(src_path, dest_path)
    if not no_success:
        print("u suck at code")
        success()



def JsonSetup(filename="LutionConfig.json", default_data=None):
    documents_dir = os.path.expanduser("~/Documents/Lution/")
    os.makedirs(documents_dir, exist_ok=True)
    file_path = os.path.join(documents_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump(default_data if default_data is not None else {}, f, indent=4)
    return file_path

def JsonSetup2(filename="Marketplace.json", default_data=None):
    documents_dir = os.path.expanduser("~/Documents/Lution/Lution Marketplace/")
    os.makedirs(documents_dir, exist_ok=True)
    file_path = os.path.join(documents_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump(default_data if default_data is not None else {}, f, indent=4)
    return file_path

def ModsFolder():
    mods_dir = os.path.expanduser("~/Documents/Lution/Mods")
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
    OpenFolder(mods_dir)




def OpenFolder(path):
    OverlaySetup()
    if platform.system() == "Darwin":  # macOS shiz
        subprocess.Popen(["open", path])
    else:  # Linux and others
        subprocess.Popen(["xdg-open", path])



def OverlaySetup():
    dest_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay")
    src_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/assets")

    os.makedirs(dest_dir, exist_ok=True)

    if os.path.isdir(src_dir):
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)


def Fontsetup():
    dest_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/fonts/")
    src_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/assets/content/fonts/")

    os.makedirs(dest_dir, exist_ok=True)

    if os.path.isdir(src_dir):
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

def ApplyMods():
    with st.spinner("Applying mods..."):
        dest_dirr = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/")
        OverwriteFolders(dest_dirr, [os.path.expanduser("~/Documents/Lution/Mods/ExtraContent/")],no_success=True)
        OverwriteFolders(dest_dirr, [os.path.expanduser("~/Documents/Lution/Mods/content/")],no_success=True)
        OverwriteFolders(dest_dirr, [os.path.expanduser("~/Documents/Lution/Mods/ClientSettings")],no_success=True)
        OverwriteFolders(dest_dirr, [os.path.expanduser("~/Documents/Lution/Mods/PlatformContent")],no_success=True)
        warn("Restart Sober to apply the mods. If you not opened Sober, you can ignore this message.")

def ApplyMarketplaceMods(dir):
    with st.spinner("Applying mods..."):
        dest_dirr = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/")
        OverwriteFolders(dest_dirr, [os.path.expanduser(f"{dir}/ExtraContent/")],no_success=True)
        OverwriteFolders(dest_dirr, [os.path.expanduser(f"{dir}/content/")],no_success=True)
        OverwriteFolders(dest_dirr, [os.path.expanduser(f"{dir}/ClientSettings")],no_success=True)
        OverwriteFolders(dest_dirr, [os.path.expanduser(f"{dir}/PlatformContent")],no_success=True)
        warn("Restart Sober to apply the mods. If you not opened Sober, you can ignore this message.")


def ResetMods():
    with st.spinner("Resetting mods..."):
        dest_dirr = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/")
        src_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/assets/content/")
        if not os.path.isdir(src_dir):
            st.warning(f"Source directory does not exist: {src_dir}")
            return
        if os.path.isdir(dest_dirr):
            shutil.rmtree(dest_dirr)
        os.makedirs(dest_dirr, exist_ok=True)
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dirr, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        success()



def ResetMods2():
    dest_dirr = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/")
    src_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/assets/content/")
    if not os.path.isdir(src_dir):
        return
    if os.path.isdir(dest_dirr):
        shutil.rmtree(dest_dirr)
    os.makedirs(dest_dirr, exist_ok=True)
    for item in os.listdir(src_dir):
        s = os.path.join(src_dir, item)
        d = os.path.join(dest_dirr, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)



def OverwriteEmoji(dest_dir):
    src_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../files/RobloxEmoji.ttf'))
    os.makedirs(dest_dir, exist_ok=True)
    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
    shutil.copy2(src_file, dest_file)





def ApplyFont():
    with st.spinner(LANG["lution.spinner.applyfont"]):
        if st.session_state.customfont:
            # setup the overlay
            Fontsetup()
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
            st.success(LANG["lution.message.success.fontapplied"])
        else:
            st.warning(LANG["lution.appearance.warning.customfontnotuploaded"])
