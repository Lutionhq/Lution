import os
import subprocess
import platform
from modules.configcheck.config import OverlaySetup 

def open_folder(path):
    OverlaySetup()
    if platform.system() == "Darwin":  # macOS shiz
        subprocess.Popen(["open", path])
    else:  # Linux and others
        subprocess.Popen(["xdg-open", path])
