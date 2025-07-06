import shutil
import subprocess
from pathlib import Path
from modules.utils.logging import log

class InstanceAlreadyExist(Exception):
    pass

class SoberManager:
    def __init__(self):
        self.name = None
        self.flatpakpath = Path("/var/lib/flatpak/app")
        self.appID = "org.vinegarhq.Sober"

    @classmethod
    def add_instance(cls, name):
        path = Path(f"~/Documents/Lution/Instances/{name}").expanduser()
        
        if path.exists():
            raise InstanceAlreadyExist(f"Instance '{name}' already exists.")
    

        log.info(f"Creating {name}", logger="MUTI INSTANCE")

        path.mkdir(parents=True, exist_ok=False)
        
        log.info(f"Created {name}", logger="MUTI INSTANCE")

    @staticmethod
    def list_instance():
        flatpakpath = Path("/var/lib/flatpak/app")
        appID = "org.vinegarhq.Sober"
        accounts = []

        if (flatpakpath / appID).exists():
            accounts.append(appID)

        for entry in flatpakpath.iterdir():
            if (
                entry.is_dir()
                and entry.name != appID
                and (entry / ".sober_instance").exists()
            ):
                accounts.append(entry.name)

        return accounts
    @staticmethod
    def run_instance(name):
        log.info(f"Launching {name}","MUTI INSTANCE")
        envpath = Path(f"~/Documents/Lution/Instances/{name}").expanduser()

        if not envpath.exists :
            envpath.mkdir(parents=True)
        
        subprocess.Popen(["env", f"HOME={envpath}", "flatpak", "run", "org.vinegarhq.Sober"])
