#src/sostrapter/modules/json/json.py
from modules.json.json import LTjson
from modules.configcheck.fontreplacer import *
from modules.utils.files import OverwriteFiles
from modules.utils.files import JsonSetup2
import os
import shutil
import os
import subprocess
import platform
import streamlit as st
import json

sysjson = LTjson()


def ApplyChanges(fpslimit, lightingtech, oof1, rpc1, rendertech, bbchat, FFlags, fontsize, useoldrobloxsounds):
    """Apply changes based on user input."""
    # Lighting Tech
    if lightingtech == "Voxel Lighting (Phase 1)" : 
        sysjson.UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",True)
        sysjson.UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",False)
        sysjson.UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",False)
    if lightingtech == "Shadowmap Lighting (Phase 2)" :
        sysjson.UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",False)
        sysjson.UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",True)
        sysjson.UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",False)
    if lightingtech == "Future Lighting (Phase 3)" :
        sysjson.UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",False)
        sysjson.UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",False)
        sysjson.UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",True)
    # FPS limit
    sysjson.UpdateFflags("DFIntTaskSchedulerTargetFps",fpslimit)
    sysjson.UpdateFflags("FFlagGameBasicSettingsFramerateCap5",False)
    sysjson.UpdateFflags("FFlagTaskSchedulerLimitTargetFpsTo2402",False)
    #Bringbackoof - ts is a hashtag lol 🥀
    sysjson.UpdateSoberConfig("bring_back_oof",oof1)
    # Disnabel Discord RPC
    sysjson.UpdateSoberConfig("discord_rpc_enabled",rpc1)
    # Render Technology
    if rendertech == "OpenGL":
        sysjson.UpdateSoberConfig("use_opengl", True)
    elif rendertech == "Vulkan":
        sysjson.UpdateSoberConfig("use_opengl", False)
    # Bubble Chat
    sysjson.UpdateSoberConfig("FFlagEnableBubbleChatFromChatService", bbchat)
    # FFlags Editor
    Currfflags = LTjson.ReadSoberConfig("fflags")
    Combine = LTjson.CombineJson(Currfflags, FFlags)
    sysjson.UpdateSoberConfig("fflags", Combine)
    # Font Size
    sysjson.UpdateFflags("FIntFontSizePadding", fontsize)
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
    sysjson.UpdateLutionConfig(key="OldRlbxSd",value=useoldrobloxsounds)
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



def LoadLightTechConfig():
    sysjson = LTjson()  # instantiate the class

    voxel = sysjson.ReadFflagsConfig("DFFlagDebugRenderForceTechnologyVoxel")
    phase2 = sysjson.ReadFflagsConfig("FFlagDebugForceFutureIsBrightPhase2")
    phase3 = sysjson.ReadFflagsConfig("FFlagDebugForceFutureIsBrightPhase3")

    if voxel:
        return "Voxel Lighting (Phase 1)"
    elif phase2:
        return "Shadowmap Lighting (Phase 2)"
    elif phase3:
        return "Future Lighting (Phase 3)"
    else:
        return "Voxel Lighting (Phase 1)"


def UsingOpenGl():
    """Load Render Tech from Sober config."""
    sysjson = LTjson()
    Open_gl = sysjson.ReadSoberConfig(key="use_opengl")
    if Open_gl:
        return True
    else:
        return False






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
        sysjson.UpdateLutionConfig(key="CursorType", value="Default")
    elif cursortype == "Old 2007 Cursor":
        OverwriteFiles(
            CursorFolder,
            [
                cursor_file("customcursor", "old2006", "ArrowCursor.png"),
                cursor_file("customcursor", "old2006", "ArrowFarCursor.png"),
                cursor_file("customcursor", "old2006", "IBeamCursor.png"),
            ]
        )
        sysjson.UpdateLutionConfig(key="CursorType", value="Old 2007 Cursor")
    elif cursortype == "Old 2013 Cursor":
        OverwriteFiles(
            CursorFolder,
            [
                cursor_file("customcursor", "old2013", "ArrowCursor.png"),
                cursor_file("customcursor", "old2013", "ArrowFarCursor.png"),
                cursor_file("customcursor", "old2013", "IBeamCursor.png"),
            ]
        )
        sysjson.UpdateLutionConfig(key="CursorType", value="Old 2013 Cursor")
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
