import os
import shutil
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