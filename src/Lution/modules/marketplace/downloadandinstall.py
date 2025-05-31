from github import Github as g
from modules.utils.files import ApplyMods
import os
import zipfile
import requests
import json

def Unzip(zip_file_path, extract_to_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_path)
        print(f"Successfully extracted '{zip_file_path}' to '{extract_to_path}'")
    except FileNotFoundError:
        print(f"Error: The file '{zip_file_path}' was not found.")
    except zipfile.BadZipFile:
        print(f"Error: The file '{zip_file_path}' is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def GHFiles(repo_name, file_path, output_path, branch="main"):
    try:
        url = f"https://raw.githubusercontent.com/{repo_name}/{branch}/{file_path}"
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Successfully downloaded '{file_path}' from '{repo_name}' to '{output_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def ApplyMarketplace(Name, type):
    repo_name = "triisdang/Lution-Mods"
    repo = g().get_repo(repo_name)
    download_dir = os.path.expanduser(f"~/Documents/Lution/Lution Marketplace/{type}s/{Name}")  
    os.makedirs(download_dir, exist_ok=True)  

    if type == "theme":
        info_file_path = "Assets/Themes/info.json"

        content = repo.get_contents(info_file_path)
        info_list = json.loads(content.decoded_content.decode())

        entry = next((item for item in info_list if item["name"] == Name), None)
        if entry:
            zip_path = entry["path"]
            local_zip_path = os.path.join(download_dir, os.path.basename(zip_path))  
            GHFiles(repo_name, zip_path, local_zip_path) 
            Unzip(local_zip_path, download_dir)  
            os.remove(local_zip_path)  
        else:
            print(f"No theme found with name '{Name}'")
        ApplyMods()

        
    elif type == "mod":
        info_file_path = "Assets/Mods/info.json"
        content = repo.get_contents(info_file_path)
        info_list = json.loads(content.decoded_content.decode())

        entry = next((item for item in info_list if item["name"] == Name), None)
        if entry:
            zip_path = entry["path"]
            local_zip_path = os.path.join(download_dir, os.path.basename(zip_path)) 
            GHFiles(repo_name, zip_path, local_zip_path)  
            Unzip(local_zip_path, download_dir) 
            os.remove(local_zip_path)  
        else:
            print(f"No mod found with name '{Name}'")
        ApplyMods()