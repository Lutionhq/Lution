#src/sostrapter/modules/json/json.py
from modules.json.json import *

def apply_changes(fpslimit, lightingtech, oof1, rpc1):
    """Apply changes based on user input."""
    # Lighting Tech
    if lightingtech == "Voxel Lighting (Phase 1)" : 
        UpdateFflags("DFFlagDebugRenderForceTechnologyVoxel",True)
    if lightingtech == "Shadowmap Lighting (Phase 2)" :
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase2",True)
    if lightingtech == "Future Lighting (Phase 3)" :
        UpdateFflags("FFlagDebugForceFutureIsBrightPhase3",True)
    # FPS limit
    UpdateFflags("DFIntTaskSchedulerTargetFps",fpslimit)
    UpdateFflags("FFlagGameBasicSettingsFramerateCap5",False)
    UpdateFflags("FFlagTaskSchedulerLimitTargetFpsTo2402",False)
    #Bringbackoof - ts is a hashtag lol 🥀
    UpdateSoberConfig("bring_back_oof",oof1)
    # Disnabel Discord RPC
    UpdateSoberConfig("discord_rpc_enabled",rpc1)


