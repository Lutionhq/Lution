#src/sostrapter/modules/json/json.py
from modules.json.json import UpdateFflags, UpdateSoberConfig,ReadFflagsConfig, ReadSoberConfig, CombineJson
from modules.configcheck.fontreplacer import *
from modules.utils.files import OverwriteFiles
from modules.utils.files import JsonSetup, JsonSetup2
import os
import shutil
import os
import subprocess
import platform
import streamlit as st
import json

def ApplyChanges(fpslimit, lightingtech, oof1, rpc1, rendertech, bbchat, FFlags, fontsize, useoldrobloxsounds):
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
    UpdateFflags("FFlagGameBasicSettingsFramerateCap5",True)
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
    # Font Size
    UpdateFflags("FIntFontSizePadding", fontsize)

    # force Overwrite meshes
    OverwriteFiles(
        os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/avatar/meshes/"),
        [
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/mesh/leftarm.mesh")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/mesh/rightarm.mesh")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/mesh/leftleg.mesh")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/mesh/rightleg.mesh")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/mesh/torso.mesh")),
        ]
    )
    # use old roblox sounds
    UpdateLutionConfig("OldRlbxSd",useoldrobloxsounds)
    if useoldrobloxsounds:
        OverwriteFiles(
            os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/sounds/"),
            [
                os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/sounds/action_footsteps_plastic.mp3")),
                os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/sounds/action_get_up.mp3")),
                os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/sounds/action_jump.mp3")),
                os.path.abspath(os.path.join(os.path.dirname(__file__), "../../files/sounds/ouch.ogg")),
            ]
        )

def Applyfflags(fflags):
    # FFlags Editor
    Currfflags = ReadSoberConfig("fflags")
    Combine = CombineJson(Currfflags, fflags)
    UpdateSoberConfig("fflags", Combine)

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




def ReadLutionConfig(key, filename="LutionConfig.json", default=None):
    JsonSetup()
    file_path = os.path.join(os.path.expanduser("~/Documents/Lution"), filename)
    if not os.path.exists(file_path):
        return default
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(key, default)

def UpdateLutionConfig(key, value, filename="LutionConfig.json"):
    JsonSetup()
    file_path = os.path.join(os.path.expanduser("~/Documents/Lution"), filename)
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
        UpdateLutionConfig("CursorType", "Default")
    elif cursortype == "Old 2007 Cursor":
        OverwriteFiles(
            CursorFolder,
            [
                cursor_file("customcursor", "old2006", "ArrowCursor.png"),
                cursor_file("customcursor", "old2006", "ArrowFarCursor.png"),
                cursor_file("customcursor", "old2006", "IBeamCursor.png"),
            ]
        )
        UpdateLutionConfig("CursorType", "Old 2007 Cursor")
    elif cursortype == "Old 2013 Cursor":
        OverwriteFiles(
            CursorFolder,
            [
                cursor_file("customcursor", "old2013", "ArrowCursor.png"),
                cursor_file("customcursor", "old2013", "ArrowFarCursor.png"),
                cursor_file("customcursor", "old2013", "IBeamCursor.png"),
            ]
        )
        UpdateLutionConfig("CursorType", "Old 2013 Cursor")
    else:
        st.error("Invalid cursor type selected.")


def ReadLutionMarketplaceConfig(key, filename="Marketplace.json", default=None):
    JsonSetup2()
    file_path = os.path.join(os.path.expanduser("~/Documents/Lution/Lution Marketplace/"), filename)
    if not os.path.exists(file_path):
        return default
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(key, default)

def UpdateLutionMarketplaceConfig(key, value, filename="Marketplace.json"):
    JsonSetup2()
    file_path = os.path.join(os.path.expanduser("~/Documents/Lution/Lution Marketplace/"), filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[key] = value
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
def RemoveLutionMarketplaceConfig(key, value_to_remove, filename="Marketplace.json"):
    JsonSetup2()
    file_path = os.path.join(os.path.expanduser("~/Documents/Lution/Lution Marketplace/"), filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    if key in data:
        values = data[key].split(',')
        values = [v.strip() for v in values]
        if value_to_remove in values:
            values.remove(value_to_remove)
            data[key] = ','.join(values)
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
        else:
            print(f"Value '{value_to_remove}' not found in key '{key}'.") # debug
    else:
        print(f"Key '{key}' not found in the dictionary.")
