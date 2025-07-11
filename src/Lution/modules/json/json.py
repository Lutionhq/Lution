#src/Lution/modules/json/json.py
import json
import os

def ReadSoberConfig(key):
    """Read a top-level value from the Sober config (outside fflags)."""
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        return config.get(key, None)
    except Exception as e:
        print(f"Failed to read setting '{key}': {e}")
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
        print(f"Failed to read fflag '{flag_name}': {e}")
        return None
def DeleteFflag(flag_name):
    """Delete a key from the fflags section of the Sober config."""
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        fflags = config.get("fflags", {})
        if flag_name in fflags:
            del fflags[flag_name]
            config["fflags"] = fflags
            with open(file_path, "w") as f:
                json.dump(config, f, indent=4)
            return True
        else:
            print(f"Flag '{flag_name}' not found in fflags.")
            return False
    except Exception as e:
        print(f"Failed to delete fflag '{flag_name}': {e}")
        return False

def UpdateFflags(flag_name, flag_value):
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            sober_config = json.load(f)
        if "fflags" not in sober_config or not isinstance(sober_config["fflags"], dict):
            sober_config["fflags"] = {}
        sober_config["fflags"][flag_name] = flag_value
        with open(file_path, "w") as f:
            json.dump(sober_config, f, indent=4)
        print(f"fflags['{flag_name}'] set to {flag_value}")
    except Exception as e:
        print(f"Failed to update fflags: {e}")

def UpdateSoberConfig(key, value):
    file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        config[key] = value
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
        print(f"Config['{key}'] set to {value}")
    except Exception as e:
        print(f"Failed to update config: {e}")

def CombineJson(*json_objs):
    """
    Combine multiple JSON objects (dicts) into one.
    Later objects overwrite earlier ones for duplicate keys.
    Skips any argument that is not a dict.
    """
    result = {}
    for obj in json_objs:
        if isinstance(obj, dict):
            result.update(obj)
        else:
            print(f"Skipped non-dict object in CombineJson: {type(obj)}")
    return result
