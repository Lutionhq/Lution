import shutil
import subprocess
from pathlib import Path
from modules.utils.logging import log

class InstanceAlreadyExist(Exception):
    pass

class SoberManager:
    def __init__(self):
        self.name = None
        self.flatpakpath = Path("/home/chip/.var/app/")
        self.appID = "org.vinegarhq.Sober"

    @classmethod
    def add_instance(cls, name):
        appID = "org.vinegarhq.Sober"
        flatpakpath = Path("/home/chip/.var/app/")

        orig = flatpakpath / appID
        instancend = f"org.vinegarhq.lution.Sober.{name}"
        new_dir = flatpakpath / instancend

        if new_dir.exists():
            raise InstanceAlreadyExist()


        shutil.copytree(orig, new_dir)
        (new_dir / ".sober_instance").touch()

        instance = cls()
        instance.UpdateMetaData(name)
        log.info(f"Account '{name}' created", "MUTI INSTANCE")
    
    @staticmethod
    def list_instance():
        flatpakpath = Path("/home/chip/.var/app/")
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

    def UpdateMetaData(self, name):
        stable_dir = self.flatpakpath / name / "x86_64" / "stable"
        if not stable_dir.exists():
            log.warn(f"Stable directory {stable_dir} does not exist yet, skipping metadata patch", "MUTI INSTANCE")
            return

        for entry in stable_dir.iterdir():
            if entry.is_dir() and entry.name != "active":
                metadata_path = entry / "metadata"
                if metadata_path.exists():
                    log.info(f"Patching metadata: {metadata_path}", "MUTI INSTANCE")
                    text = metadata_path.read_text()
                    text = text.replace("name=org.vinegarhq.Sober", f"name={name}")
                    metadata_path.write_text(text)
                    return

        log.error("Metadata file not found for patching", "MUTI INSTANCE")
