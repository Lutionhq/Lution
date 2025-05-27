#src/sostrapter/modules/json/json.py
import json
import os
import streamlit as st

def ReadSoberConfig(key):
    """Read a top-level value from the Sober config (outside fflags)."""
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        return config.get(key, None)
    except Exception as e:
        st.error(f"Failed to read setting '{key}': {e}")
        return None

def ReadFflagsConfig(flag_name):
    """Read a value from the fflags section of the Sober config."""
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        fflags = config.get("fflags", {})
        return fflags.get(flag_name, None)
    except Exception as e:
        st.error(f"Failed to read fflag '{flag_name}': {e}")
        return None
def UpdateFflags(flag_name, flag_value):
    try:
        if "fflags" not in sober_config or not isinstance(sober_config["fflags"], dict):
            sober_config["fflags"] = {}
        sober_config["fflags"][flag_name] = flag_value
        with open(file_path, "w") as f:
            json.dump(sober_config, f, indent=4)
        st.success(f"fflags['{flag_name}'] set to {flag_value}")
    except Exception as e:
        st.error(f"Failed to update fflags: {e}")

def UpdateSoberConfig(key, value):
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        config[key] = value
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
        st.success(f"Config['{key}'] set to {value}")
    except Exception as e:
        st.error(f"Failed to update config: {e}")