import shutil
import subprocess
import shutil
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
        log.info(f"Adding {name} to the list", logger="MUTI INSTANCE")

        cls.update_instance(name)

        log.info(f"Created {name}", logger="MUTI INSTANCE")

    @staticmethod
    def list_instance():
        log.info("Getting Instance list..",logger="MUTI INSTANCE")
        file_path = Path("~/Documents/Lution/Instances/Instances.list").expanduser()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            with open(file_path, 'r') as file:
                content = file.read().strip()
                instances = ast.literal_eval(content) if content else []
        else:
            instances = []

        return instances

    @staticmethod
    def delete_instance(name):
        """Delete a instance"""
        log.info(f"Deleting {name}",logger="MUTI INSTANCE")

        instancefolder = Path(f"~/Documents/Lution/Instances/{name}").expanduser()
        file_path = Path("~/Documents/Lution/Instances/Instances.list").expanduser()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            with open(file_path, 'r') as file:
                content = file.read().strip()
                instances = ast.literal_eval(content) if content else []
        else:
            instances = []

        shutil.rmtree(instancefolder)
        instances.remove(name)

        with open(file_path, 'w') as file:
            file.write(str(instances))

        log.info(f"Done",logger="MUTI INSTANCE")


    def run_instance(name):
        log.info(f"Launching {name}","MUTI INSTANCE")
        envpath = Path(f"~/Documents/Lution/Instances/{name}").expanduser()

        if not envpath.exists :
            envpath.mkdir(parents=True)
        # 
        subprocess.Popen(["env", f"HOME={envpath}", "flatpak", "run", "org.vinegarhq.Sober"]).wait()
        subprocess.Popen(f"env HOME={envpath} flatpak override --user --filesystem=xdg-run/app/com.discordapp.Discord:create --filesystem=xdg-run/discord-ipc-0 org.vinegarhq.Sober", shell=True)

    def update_instance(name):
        """Update a list of instances stored in a file"""

        log.info(f"Updating to {name}")

        file_path = Path("~/Documents/Lution/Instances/Instances.list").expanduser()
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
