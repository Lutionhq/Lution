#src/Luiton/modules/utils/lang.py
import os
import json
import streamlit as st

file_path = os.path.expanduser("~/.var/app/org.vinegarhq.Sober/config/sober/config.json")
LANG_DIR = os.path.join(os.path.dirname(__file__), "files/languages")  
lang_files = [f for f in os.listdir(LANG_DIR) if f.endswith(".json")]
LANG_CODES = [os.path.splitext(f)[0] for f in lang_files]
LANG_NAMES = {
    "en": "English",
    "vn": "Tiếng Việt",
    "ger": "Deutsch",
    "lolcat" : "Lolcat 😹 ",
    "premiumenglish": "𝓟𝓻𝓮𝓶𝓲𝓾𝓶  𝓔𝓷𝓰𝓵𝓲𝓼𝓱",
    "tram" : "🚡🚡🚡🚡🚡"

}
lang_path = os.path.join(LANG_DIR, f"{st.session_state.language}.json")
with open(lang_path, "r") as f:
    LANG = json.load(f)
try:
    with open(file_path, 'r') as f:
        sober_config = json.load(f)
except FileNotFoundError:
    st.sidebar.error(LANG[f"lution.message.error.filenotfound"])
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    st.sidebar.error(LANG[f"lution.message.error.jsondecode"])
    print(f"Error: Could not decode JSON from the file '{file_path}'.")
except Exception as e:
    st.sidebar.error(LANG["lution.message.error.unknown"])
    print(f"An unexpected error occurred: {e}")
