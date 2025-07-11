from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio 

@Gtk.Template(resource_path='/org/wookhq/Lution/ui/window.ui')
class LutionWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'LutionWindow'

    view_stack = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Load page_fflags.ui from the GResource
        builder2 = Gtk.Builder()
        builder2.add_from_resource("/org/wookhq/Lution/ui/page_fflags.ui") # <-- Changed here
        page_fflags = builder2.get_object("page_fflags")
        self.view_stack.add_titled(page_fflags, "fflags", "FFlags")

    @Gtk.Template.Callback()
    def on_home_clicked(self, button):
        self.view_stack.set_visible_child_name("home")

    @Gtk.Template.Callback()
    def on_fflag_clicked(self, button):
        self.view_stack.set_visible_child_name("fflags")