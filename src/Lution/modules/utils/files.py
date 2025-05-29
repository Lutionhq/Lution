import os
import shutil
import json
import subprocess
import platform
from .messages import success


def OverwriteFiles(dest_dir, src_files):
    os.makedirs(dest_dir, exist_ok=True)

    for src_path in src_files:
        if not os.path.isabs(src_path):
            raise ValueError(f"Expected absolute path, got: {src_path}")

        if not os.path.isfile(src_path):
            raise FileNotFoundError(f"Source file does not exist: {src_path}")

        filename = os.path.basename(src_path)
        dest_path = os.path.join(dest_dir, filename)

        shutil.copy2(src_path, dest_path)
    success()

def JsonSetup(filename="LutionConfig.json", default_data=None):
    documents_dir = os.path.expanduser("~/Documents/Lution/")
    os.makedirs(documents_dir, exist_ok=True)
    file_path = os.path.join(documents_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump(default_data if default_data is not None else {}, f, indent=4)
    return file_path

def ModsFolder():
    mods_dir = os.path.expanduser("~/Documents/Lution/Mods")
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
    OpenFolder


def OpenFolder(path):
    from modules.configcheck.config import OverlaySetup
    OverlaySetup()
    if platform.system() == "Darwin":  # macOS shiz
        subprocess.Popen(["open", path])
    else:  # Linux and others
        subprocess.Popen(["xdg-open", path])