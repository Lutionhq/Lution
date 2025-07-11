import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import sys

print("Python script started.")

try:
    class TestApplication(Adw.Application):
        def __init__(self):
            super().__init__(application_id="org.example.TestApp")

        def do_activate(self):
            print("Application activated. Creating window.")
            win = Gtk.ApplicationWindow(application=self)
            win.set_title("Test App")
            win.set_default_size(300, 200)
            win.present()
            print("Window presented.")

    app = TestApplication()
    print("Application instance created. Running app.")
    exit_status = app.run(sys.argv)
    print(f"Application exited with status: {exit_status}")

except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)

print("Python script finished.")