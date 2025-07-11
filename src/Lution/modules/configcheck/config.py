#src/sostrapter/modules/json/json.py
from modules.json.json import UpdateFflags, UpdateSoberConfig,ReadFflagsConfig, ReadSoberConfig, CombineJson, DeleteFflag
from modules.configcheck.fontreplacer import *
from modules.utils.files import OverwriteFiles
from modules.utils.files import JsonSetup, JsonSetup2
import os
import shutil
import os
import subprocess
import platform
from gi.repository import Gio
import json

def ApplyChanges(
    fpslimit=None, lightingtech=None, oof1=None, rpc1=None, 
    rendertech=None, bbchat=None, fontsize=None, 
    useoldrobloxsounds=None, disableprsh=None, 
    texturequa=None, msaa=None
):
    if lightingtech:
        if lightingtech == "Voxel Lighting (Phase 1)":
            UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel", True)
            UpdateFflags("FFlagDebugForceFutureIsBrightPhase2", False)
            UpdateFflags("FFlagDebugForceFutureIsBrightPhase3", False)
        elif lightingtech == "Shadowmap Lighting (Phase 2)":
            UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel", False)
            UpdateFflags("FFlagDebugForceFutureIsBrightPhase2", True)
            UpdateFflags("FFlagDebugForceFutureIsBrightPhase3", False)
        elif lightingtech == "Future Lighting (Phase 3)":
            UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel", False)
            UpdateFflags("FFlagDebugForceFutureIsBrightPhase2", False)
            UpdateFflags("FFlagDebugForceFutureIsBrightPhase3", True)

    if texturequa:
        UpdateFflags("DFFlagTextureQualityOverrideEnabled", True)
        match texturequa:
            case "Off":
                DeleteFflag("DFFlagTextureQualityOverrideEnabled")
                DeleteFflag("DFIntTextureQualityOverride")
            case "Level 0 (potato)":
                UpdateFflags("DFIntTextureQualityOverride", 0)
            case "Level 1 (Low)":
                UpdateFflags("DFIntTextureQualityOverride", 1)
            case "Level 2 (Medium)":
                UpdateFflags("DFIntTextureQualityOverride", 2)
            case "Level 3 (High)":
                UpdateFflags("DFIntTextureQualityOverride", 3)
            case "Level 4 (Ultra)":
                UpdateFflags("DFIntTextureQualityOverride", 4)

    if msaa:
        UpdateFflags("FFlagDebugDisableMSAA", False)
        match msaa:
            case "Off (MSAA)":
                UpdateFflags("DFFlagTextureQualityOverrideEnabled", True)
                DeleteFflag("FIntMSAASampleCount")
            case "x1 (MSAA)":
                UpdateFflags("FIntMSAASampleCount", 1)
            case "x2 (MSAA)":
                UpdateFflags("FIntMSAASampleCount", 2)
            case "x4 (MSAA)":
                UpdateFflags("FIntMSAASampleCount", 4)
            case "Auto (MSAA)":
                DeleteFflag("DFIntTextureQualityOverride")

    if fpslimit is not None:
        UpdateFflags("DFIntTaskSchedulerTargetFps", fpslimit)
        UpdateFflags("FFlagGameBasicSettingsFramerateCap5", True)
        UpdateFflags("FFlagTaskSchedulerLimitTargetFpsTo2402", False)

    if oof1 is not None:
        UpdateSoberConfig("bring_back_oof", oof1)

    if rpc1 is not None:
        UpdateSoberConfig("discord_rpc_enabled", rpc1)

    if disableprsh is not None:
        if disableprsh:
            UpdateFflags("FIntRenderShadowIntensity", "0")
        else:
            UpdateFflags("FIntRenderShadowIntensity", "75")

    if rendertech:
        if rendertech == "OpenGL":
            UpdateSoberConfig("use_opengl", True)
        elif rendertech == "Vulkan":
            UpdateSoberConfig("use_opengl", False)

    if bbchat is not None:
        UpdateFflags("FFlagEnableBubbleChatFromChatService", bbchat)

    if fontsize is not None:
        UpdateFflags("FIntFontSizePadding", fontsize)


    if useoldrobloxsounds is not None:
        UpdateLutionConfig("OldRlbxSd", useoldrobloxsounds)

        if useoldrobloxsounds:
            sound_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/sounds/")
            os.makedirs(sound_path, exist_ok=True)

            for name in Gio.resources_enumerate_children("/org/wookhq/Lution/boostraper/sounds", Gio.ResourceLookupFlags.NONE) or []:
                data = Gio.resources_lookup_data(f"/org/wookhq/Lution/boostraper/sounds/{name}", Gio.ResourceLookupFlags.NONE)
                with open(os.path.join(sound_path, name), "wb") as f:
                    f.write(data.get_data())


def Applyfflags(fflags):
    if isinstance(fflags, str):
        try:
            fflags = json.loads(fflags)
        except json.JSONDecodeError:
            log.error("Invalid JSON passed to Applyfflags")
            return

    current_raw = ReadSoberConfig("fflags")
    try:
        current = json.loads(current_raw) if isinstance(current_raw, str) else current_raw
    except json.JSONDecodeError:
        current = {}

    if not isinstance(current, dict):
        current = {}

    if not isinstance(fflags, dict):
        log.error("Parsed fflags is not a dict")
        return

    combined = {**current, **fflags}
    UpdateSoberConfig("fflags", combined)


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
    gresource_prefix = "/org/wookhq/Lution/boostraper/customcursor"
    dest = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/content/textures/Cursors/KeyboardMouse")

    def write_cursor_file(folder, name):
        gresource_path = f"{gresource_prefix}/{folder}/{name}"
        data = Gio.resources_lookup_data(gresource_path, Gio.ResourceLookupFlags.NONE).get_data()
        with open(os.path.join(dest, name), "wb") as f:
            f.write(data)

    if cursortype == "Default":
        for fname in ["ArrowCursor.png", "ArrowFarCursor.png", "IBeamCursor.png"]:
            write_cursor_file("new", fname)
        UpdateLutionConfig("CursorType", "Default")

    elif cursortype == "Old 2007 Cursor":
        for fname in ["ArrowCursor.png", "ArrowFarCursor.png", "IBeamCursor.png"]:
            write_cursor_file("old2006", fname)
        UpdateLutionConfig("CursorType", "Old 2007 Cursor")

    elif cursortype == "Old 2013 Cursor":
        for fname in ["ArrowCursor.png", "ArrowFarCursor.png", "IBeamCursor.png"]:
            write_cursor_file("old2013", fname)
        UpdateLutionConfig("CursorType", "Old 2013 Cursor")

    else:
        print("Invalid cursor type selected.")


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
