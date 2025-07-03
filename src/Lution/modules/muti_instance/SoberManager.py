import shutil
import subprocess
from pathlib import Path
from modules.utils.logging import *



# Original from DiM, forked by chip
class SoberManager():
    def __init__(self):
        self.name = None
        self.flatpakpath = Path("/var/lib/flatpak/app")
        self.appID = "org.vinegarhq.Sober"
    
    @classmethod
    def add_instance(cls, name):
        """Add an Instance."""
        appID = "org.vinegarhq.Sober"
        flatpakpath = Path("/var/lib/flatpak/app")
        
        orig = flatpakpath / appID
        new_dir = flatpakpath / name

        if new_dir.exists() :
            raise InstanceAlreadyExist

        if not orig.exists():
            warn("Sober not installed, installing..", "MUTI INSTANCE")
            subprocess.run(["flatpak", "install", "--user", cls.appID, "-y"], check=True)

        shutil.copytree(orig, new_dir)

        # Mark this folder as our created instance
        (new_dir / ".sober_instance").touch()
        
        cls.UpdateMetaData(name)
        print(f"Account '{cls.name}' created")
    

    def UpdateMetaData(self, name):
        stable_dir = self.path / name / "x86_64" / "stable"
        if not stable_dir.exists():
            warn(f"Stable directory {stable_dir} does not exist yet, skipping metadata patch","MUTI INSTANCE")
            return

        for entry in stable_dir.iterdir():
            if entry.is_dir() and entry.name != "active":
                possible_metadata = entry / "metadata"
                if possible_metadata.exists():
                    info(f"Patching metadata: {possible_metadata}","MUTI INSTANCE")
                    text = possible_metadata.read_text()
                    text = text.replace(f"name={account_name}") # remove appid
                    possible_metadata.write_text(text)
                    return

        error("Metadata file not found for patching", "MUTI INSTANCE")