#src/sostrapter/modules/json/json.py
from modules.json.json import UpdateFflags, UpdateSoberConfig,ReadFflagsConfig, ReadSoberConfig, CombineJson
from modules.configcheck.fontreplacer import *
from modules.utils.files import OverwriteFiles
import os
import shutil
import os
import subprocess
import platform
import streamlit as st
import json

def apply_changes(fpslimit, lightingtech, oof1, rpc1, rendertech, bbchat, FFlags, fontsize, Cursor):
    """Apply changes based on user input."""
    # Lighting Tech
    if lightingtech == "Voxel Lighting (Phase 1)" : 
        UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",True)
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",False)
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",False)
    if lightingtech == "Shadowmap Lighting (Phase 2)" :
        UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",False)
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",True)
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",False)
    if lightingtech == "Future Lighting (Phase 3)" :
        UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",False)
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",False)
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",True)
    # FPS limit
    UpdateFflags("DFIntTaskSchedulerTargetFps",fpslimit)
    UpdateFflags("FFlagGameBasicSettingsFramerateCap5",False)
    UpdateFflags("FFlagTaskSchedulerLimitTargetFpsTo2402",False)
    #Bringbackoof - ts is a hashtag lol 🥀
    UpdateSoberConfig("bring_back_oof",oof1)
    # Disnabel Discord RPC
    UpdateSoberConfig("discord_rpc_enabled",rpc1)
    # Render Technology
    if rendertech == "OpenGL":
        UpdateSoberConfig("use_opengl", True)
    elif rendertech == "Vulkan":
        UpdateSoberConfig("use_opengl", False)
    # Bubble Chat
    UpdateSoberConfig("FFlagEnableBubbleChatFromChatService", bbchat)
    # FFlags Editor
    Currfflags = ReadSoberConfig("fflags")
    Combine = CombineJson(Currfflags, FFlags)
    UpdateSoberConfig("fflags", Combine)
    # Font Size
    UpdateFflags("FIntFontSizePadding", fontsize)



def LoadLightTechConfig():
    """Load Lighting techs Sober configs into session state."""
    Voxel = ReadFflagsConfig("DFFlagDebugRenderForceTechnologyVoxel")
    Phase2 = ReadFflagsConfig("FFlagDebugForceFutureIsBrightPhase2")
    Phase3 = ReadFflagsConfig("FFlagDebugForceFutureIsBrightPhase3")
    if Voxel:
        return "Voxel Lighting (Phase 1)"
    elif Phase2:
        return "Shadowmap Lighting (Phase 2)"
    elif Phase3:
        return "Future Lighting (Phase 3)"
    else:
        return "Voxel Lighting (Phase 1)"  # Default fallback

def UsingOpenGl():
    """Load Render Tech from Sober config."""
    Open_gl = ReadSoberConfig("use_opengl")
    if Open_gl:
        return True
    else:
        return False

def OverlaySetup():
    dest_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content")
    src_dir = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/assets/content")
    
    if os.path.isdir(dest_dir):
        return

    os.makedirs(dest_dir, exist_ok=True)

    if os.path.isdir(src_dir):
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

def open_folder(path):
    OverlaySetup()
    if platform.system() == "Darwin":  # macOS shiz
        subprocess.Popen(["open", path])
    else:  # Linux and others
        subprocess.Popen(["xdg-open", path])

def JsonSetup(filename="LutionConfig.json", default_data=None):
    documents_dir = os.path.expanduser("~/Documents")
    os.makedirs(documents_dir, exist_ok=True)
    file_path = os.path.join(documents_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump(default_data if default_data is not None else {}, f, indent=4)
    return file_path


def ReadLutionConfig(key, filename="LutionConfig.json", default=None):
    JsonSetup()
    file_path = os.path.join(os.path.expanduser("~/Documents"), filename)
    if not os.path.exists(file_path):
        return default
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(key, default)

def UpdateLutionConfig(key, value, filename="LutionConfig.json"):
    JsonSetup()
    file_path = os.path.join(os.path.expanduser("~/Documents"), filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[key] = value
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def UpdateCursor(cursortype):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files"))
    CursorFolder = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/textures/Cursors/KeyboardMouse")

    def cursor_file(*parts):
        return os.path.join(base_dir, *parts)

    if cursortype == "Default":
        OverwriteFiles(
            CursorFolder,
            [
                cursor_file("customcursor", "new", "ArrowCursor.png"),
                cursor_file("customcursor", "new", "ArrowFarCursor.png"),
                cursor_file("customcursor", "new", "IBeamCursor.png"),
            ]
        )
    elif cursortype == "Old 2007 Cursor":
        OverwriteFiles(
            CursorFolder,
            [
                cursor_file("customcursor", "old", "ArrowCursor.png"),
                cursor_file("customcursor", "old", "ArrowFarCursor.png"),
                cursor_file("customcursor", "old", "IBeamCursor.png"),
            ]
        )
    else:
        st.error("Invalid cursor type selected.")
