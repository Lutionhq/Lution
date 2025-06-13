#src/Lution/modules/json/json.py
import json
import os
import streamlit as st
from modules.utils.files import JsonSetup

class LTjson:
    def __init__(self):
        using = self.ReadLutionConfig(key="Using")
        # print(using)
        if using == "equinox" :
            self.robloxpath = "tell tray to do the accet overlay for equinox"
            self.file_path = os.path.expanduser("@xtrayambak on discord now!111")
        if using == "sober" :
            self.robloxpath = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/data/sober/asset_overlay/")
            self.file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")


    def ReadSoberConfig(self, key):
        try:
            with open(self.file_path, "r") as f:
                config = json.load(f)
            return config.get(key)
        except Exception as e:
            st.error(f"Failed to read setting '{key}': {e}")
            return None

    def ReadFflagsConfig(self, flag_name):
        try:
            with open(self.file_path, "r") as f:
                config = json.load(f)
            return config.get("fflags", {}).get(flag_name)
        except Exception as e:
            st.error(f"Failed to read fflag '{flag_name}': {e}")
            return None

    def UpdateFflags(self, flag_name, flag_value):
        try:
            with open(self.file_path, "r") as f:
                config = json.load(f)
            config.setdefault("fflags", {})[flag_name] = flag_value
            with open(self.file_path, "w") as f:
                json.dump(config, f, indent=4)
            st.success(f"fflags['{flag_name}'] set to {flag_value}")
        except Exception as e:
            st.error(f"Failed to update fflags: {e}")

    def UpdateSoberConfig(self, key, value):
        try:
            with open(self.file_path, "r") as f:
                config = json.load(f)
            config[key] = value
            with open(self.file_path, "w") as f:
                json.dump(config, f, indent=4)
            st.success(f"Config['{key}'] set to {value}")
        except Exception as e:
            st.error(f"Failed to update config: {e}")

    def CombineJson(self, *json_objs):
        result = {}
        for obj in json_objs:
            if isinstance(obj, dict):
                result.update(obj)
            else:
                st.warning(f"Skipped non-dict object in combine_json: {type(obj)}")
        return result

    def ReadLutionConfig(self, key, filename="LutionConfig.json", default=None):
        JsonSetup()
        file_path = os.path.join(os.path.expanduser("~/Documents/Lution"), filename)
        if not os.path.exists(file_path):
            return default
        with open(file_path, "r") as f:
            data = json.load(f)
        return data.get(key, default)

    def UpdateLutionConfig(self, key, value, filename="LutionConfig.json"):
        JsonSetup()
        file_path = os.path.join(os.path.expanduser("~/Documents/Lution"), filename)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = json.load(f)
        else:
            data = {}
        data[key] = value
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
