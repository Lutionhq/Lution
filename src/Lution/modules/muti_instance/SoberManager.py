import shutil
import subprocess
from pathlib import Path
import ast
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
        file_path = Path("~/Documents/Lution/Instances.list").expanduser()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            with open(file_path, 'r') as file:
                content = file.read().strip()
                instances = ast.literal_eval(content) if content else []
        else:
            instances = []

    def run_instance(name):
        log.info(f"Launching {name}","MUTI INSTANCE")
        envpath = Path(f"~/Documents/Lution/Instances/{name}").expanduser()

        if not envpath.exists :
            envpath.mkdir(parents=True)
        
        subprocess.Popen(["env", f"HOME={envpath}", "flatpak", "run", "org.vinegarhq.Sober"])
    
    def update_instance(name):
        """Update a list of instances stored in a file"""

        file_path = Path("~/Documents/Lution/Instances.list").expanduser()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            with open(file_path, 'r') as file:
                content = file.read().strip()
                instances = ast.literal_eval(content) if content else []
        else:
            instances = []

        instances.append(name)

        with open(file_path, 'w') as file:
            file.write(str(instances))
