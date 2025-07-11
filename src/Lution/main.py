import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw

print("DEBUG: Lution main.py started.") # NEW: Start of script
resource_path = "/usr/local/share/org.wookhq.Lution/org.wookhq.Lution.gresource"
print(f"DEBUG: Attempting to load GResource from: {resource_path}") # NEW: Path check

try:
    loaded_resource = Gio.Resource.load(resource_path)
    Gio.resources_register(loaded_resource)
    print("DEBUG: GResource loaded and registered successfully.")
except Exception as e:
    print(f"ERROR: Failed to load or register GResource: {e}", file=sys.stderr)
    import traceback # NEW: To print full traceback
    traceback.print_exc(file=sys.stderr) # NEW: Print traceback
    sys.exit(1)

# Ensure window import is *after* resource registration
from window import LutionWindow

class LutionApplication(Adw.Application):
    def __init__(self):
        print("DEBUG: LutionApplication __init__ called.")
        # Ensure application_id matches your .desktop file and resource prefix
        super().__init__(application_id='org.wookhq.Lution',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/org/wookhq/Lution') # This base path is critical for templates
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        print("DEBUG: LutionApplication __init__ finished.")

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = LutionWindow(application=self)
        win.present()

    def on_about_action(self, *args):
        about = Adw.AboutDialog(application_name='Lution',
                                application_icon='org.wookhq.Lution',
                                developer_name='The Wookq Shit',
                                version='1.2.3',
                                developers=['Chip'],
                                copyright='© 2025 Lution')
        about.set_translator_credits("") 
        about.present(self.props.active_window)

    def on_preferences_action(self, widget, _):
        print('DEBUG: app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

def main(version):
    print("DEBUG: main function called.")
    app = LutionApplication()
    print("DEBUG: LutionApplication instance created.")
    return app.run(sys.argv)

if __name__ == '__main__':
    print("DEBUG: Script started from __main__.")
    sys.exit(main("0.1.0"))