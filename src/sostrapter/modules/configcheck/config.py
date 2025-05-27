#src/sostrapter/modules/json/json.py
from modules.json.json import UpdateFflags, UpdateSoberConfig,ReadFflagsConfig, ReadSoberConfig

def apply_changes(fpslimit, lightingtech, oof1, rpc1,rendertech):
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