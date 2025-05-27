#src/sostrapter/modules/json/json.py
from modules.json.json import UpdateFflags, UpdateSoberConfig,ReadFflagsConfig, ReadSoberConfig
from modules.configcheck.fontreplacer import *
import os
import shutil
import os
import subprocess
import platform

def apply_changes(fpslimit, lightingtech, oof1, rpc1, rendertech, bbchat, cusfont):
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
    # Custom Font
    UpdateSoberConfig("custom_font", "~/Documents/font test")


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
