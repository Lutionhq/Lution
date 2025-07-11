# src/Lution/modules/utils/lang.py
import json
from gi.repository import Gio # Import Gio to work with GResources


GRESOURCE_LANG_BASE_PATH = "/org/wookhq/Lution/boostraper/languages"


LANG_CODES = ["en", "ger", "lolcat", "premiumenglish", "tram", "vn"]

LANG_NAMES = {
    "en": "English",
    "vn": "Tiếng Việt",
    "ger": "Deutsch",
    "lolcat" : "Lolcat 😹 ",
    "premiumenglish": "�𝓻𝓮𝓶𝓲𝓾𝓶  𝓔𝓷𝓰𝓵𝓲𝓼𝓱",
    "tram" : "🚡🚡🚡🚡🚡"
}

def read_lang_from_resource(lang_code):
    resource_path = f"{GRESOURCE_LANG_BASE_PATH}/{lang_code}.json"
    
    try:
        data = Gio.resources_lookup_data(resource_path, Gio.ResourceFlags.NONE)
        
        json_string = data.get_data().decode('utf-8')
        
        return json.loads(json_string)
    except Exception as e:
        print(f"ERROR: Could not load language '{lang_code}' from GResource: {e}")
        return {}


LANG = read_lang_from_resource("en") # Load English as a default for initial imports
