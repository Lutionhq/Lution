import json
import os
import streamlit as st

class LTjson:
    robloxpath = "sigmapath"
    def __init__(self):
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
