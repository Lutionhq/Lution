import json
from modules.utils.lang import LANG
from modules.utils.logging import log
from modules.utils.files import OverlaySetup
from modules.configcheck.config import ReadSoberConfig, Applyfflags, ReadFflagsConfig, ApplyChanges
from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/wookhq/Lution/ui/window.ui')
class LutionWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'LutionWindow'

    view_stack = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        builder = Gtk.Builder() # Create a new builder instance
        builder.add_from_resource("/org/wookhq/Lution/ui/page_fflags.ui")
        page_fflags = builder.get_object("page_fflags")

        # CORE FFLAGS
        self.view_stack.add_titled(page_fflags, "fflags", "FFlags")
        self._oof_toggle = builder.get_object("oof_toggle")
        if self._oof_toggle:
            value = ReadSoberConfig("bring_back_oof")
            self._oof_toggle.set_active(value)
            self._oof_toggle.connect("notify::active", self._on_oof_toggle_changed)
        
        self._rpc_toggle = builder.get_object("rpc_toggle")
        if self._rpc_toggle:
            value = ReadSoberConfig("discord_rpc_enabled")
            self._rpc_toggle.set_active(value)
            self._rpc_toggle.connect("notify::active", self._on_rpc_toggle_changed)

        self._fps_limit_textbox = builder.get_object("fpslimit_entry")
        if self._fps_limit_textbox:
            value = ReadFflagsConfig("DFIntTaskSchedulerTargetFps")
            self._fps_limit_textbox.set_text(str(value))
            self._fps_limit_textbox.connect("changed", self._on_fps_limit_changed)
        
        self._render_dropdown = builder.get_object("render_dropdown")
        if self._render_dropdown:
            model = self._render_dropdown.get_model()
            if model:
                value = ReadSoberConfig("use_opengl")
                if value:
                    self._render_dropdown.set_selected(2)
                else:
                    self._render_dropdown.set_selected(1)
            self._render_dropdown.connect("notify::selected", self.on_rendertech_changed)
        
        self._tech_dropdown = builder.get_object("lightingtech_dropdown")
        if self._tech_dropdown:
            model = self._tech_dropdown.get_model()
            if model:
                Voxel = ReadFflagsConfig("DFFlagDebugRenderForceTechnologyVoxel")
                Shadowmap = ReadFflagsConfig("FFlagDebugForceFutureIsBrightPhase2")
                Future = ReadFflagsConfig("FFlagDebugForceFutureIsBrightPhase3")
                if Voxel and not Shadowmap and not Future:
                    self._tech_dropdown.set_selected(0)
                if Shadowmap and not Voxel and not Future:
                    self._tech_dropdown.set_selected(1)
                if Future and not Future and not Voxel:
                    self._tech_dropdown.set_selected(2)
        self._tech_dropdown.connect("notify::selected", self.on_lightingtech_changed)
        
        # END
        
        # PRESET
        self._disnable_chat_toggle = builder.get_object("disablechat_toggle")
        if self._disnable_chat_toggle:
            value = ReadFflagsConfig("FFlagEnableBubbleChatFromChatService")
            self._disnable_chat_toggle.set_active(value)
        self._disnable_chat_toggle.connect("notify::active", self._on_disnable_chat_)


        self.disnable_player_sh_toggle = builder.get_object("disableplayersh_toggle")
        if self.disnable_player_sh_toggle:
            value = ReadFflagsConfig("FFlagEnableBubbleChatFromChatService")
            if value == 0:
                self.disnable_player_sh_toggle.set_active(True)
            else:
                self.disnable_player_sh_toggle.set_active(False)
        self.disnable_player_sh_toggle.connect("notify::active", self._on_disnable_plrshadow)


        self._font_size_textbox = builder.get_object("fontsize_entry")
        if self._font_size_textbox:
            value = ReadFflagsConfig("FIntFontSizePadding")
            self._font_size_textbox.set_text(str(value))
        self._font_size_textbox.connect("changed", self._on_font_size_changed)

        self._msaa_dropdown = builder.get_object("msaa_dropdown")
        if self._msaa_dropdown:
            flag1 = ReadFflagsConfig("FFlagDebugDisableMSAA")
            flag2 = ReadFflagsConfig("FIntMSAASampleCount")
            if not flag1:
                self._msaa_dropdown.set_selected(0)
            else:
                value = flag2 + 2
                self._msaa_dropdown.set_selected(value)
        self._msaa_dropdown.connect("notify::selected", self._on_msaa_changed)
        
        self._texture_quality_dropdown = builder.get_object("texturequality_dropdown") 
        if self._texture_quality_dropdown:
            value = ReadFflagsConfig("DFIntTextureQualityOverride")
            shifted = int(value) + 1
            self._texture_quality_dropdown.set_selected(shifted)
            self._texture_quality_dropdown.connect("notify::selected", self._on_texture_quality_changed)

        # END


    # CORE FFLAG
    def _on_oof_toggle_changed(self, toggle_button, gparam_spec):
        is_active = toggle_button.get_active()
        log.info(f"OOF Toggle changed: {is_active}")
        ApplyChanges(oof1=is_active)
    def _on_rpc_toggle_changed(self, toggle_button, gparam_spec):
        is_active = toggle_button.get_active()
        log.info(f"RPC Toggle Changed : {is_active}")
        ApplyChanges(rpc1=is_active)
    def _on_fps_limit_changed(self, entry):
        text = entry.get_text()
        try :
            fps = int(text)
            ApplyChanges(fpslimit=fps)
        except ValueError:
            pass
    
    def on_rendertech_changed(self, dropdown, pram):
        value = dropdown.get_selected_item().get_string()
        log.info(f"Render tech changed : {value}")
        ApplyChanges(rendertech=value)
    
    def on_lightingtech_changed(self, dropdown, pram):
        value = dropdown.get_selected_item().get_string()
        log.info(f"Lighting tech changed : {value}")
        ApplyChanges(lightingtech=value)
    
    def _on_font_size_changed(self, entry):
        text = entry.get_text()
        try : 
            value = int(text)
            ApplyChanges(fontsize=value)
        except ValueError:
            pass

    # PRESET
    def _on_disnable_chat_ (self, toggle_button, gparam_spec):
        is_active = toggle_button.get_active()
        log.info(f"Disnable chat changed : {is_active}")
        ApplyChanges(bbchat=is_active)    

    def _on_disnable_plrshadow(self, toggle_button, gparam_spec):
        is_active = toggle_button.get_active()
        log.info(f"Disnable plyr shadow changed : {is_active}")
        ApplyChanges(disableprsh=is_active)
    
    def _on_msaa_changed(self, dropdown, pram):
        value = dropdown.get_selected_item().get_string()
        log.info(f"MSAA changed : {value}")
        ApplyChanges(msaa=value)
    
    def _on_texture_quality_changed(self, dropdown, pram):
        value = dropdown.get_selected_item().get_string()
        log.info(f"Texture quality changed : {value}")
        ApplyChanges(texturequa=value)


    # END

    @Gtk.Template.Callback()
    def on_home_clicked(self, button):
        self.view_stack.set_visible_child_name("home")

    @Gtk.Template.Callback()
    def on_fflag_clicked(self, button):
        self.view_stack.set_visible_child_name("fflags")
