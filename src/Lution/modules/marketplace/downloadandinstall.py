from github import Github as g
from modules.utils.files import ApplyMarketplaceMods
import os
import zipfile
import requests
import json
import time

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

def GHFiles(repo_name, file_path, output_path, max_retries=3, retry_delay=5):
    repo = g().get_repo(repo_name)

    for attempt in range(max_retries):
        try:
            print(f"Attempting to download '{file_path}' from '{repo_name}' (Attempt {attempt + 1}/{max_retries})")
            contents = repo.get_contents(file_path, ref="main") 

            if contents:
                with open(output_path, "wb") as f:
                    f.write(contents.decoded_content)  
                print(f"Successfully downloaded '{file_path}' from '{repo_name}' to '{output_path}'")
                return
            else:
                raise FileNotFoundError(f"File '{file_path}' not found in repository '{repo_name}'")

        except Exception as e:
            print(f"Download failed (Attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Max retries reached. Download failed.")
                raise

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
            if zipfile.is_zipfile(local_zip_path):
                Unzip(local_zip_path, download_dir)
                os.remove(local_zip_path)
            else:
                print(f"Error: {local_zip_path} is not a valid zip file.")
        else:
            print(f"No theme found with name '{Name}'")
        ApplyMarketplaceMods(download_dir)

    elif type == "mod":
        info_file_path = "Assets/Mods/info.json"
        content = repo.get_contents(info_file_path)
        info_list = json.loads(content.decoded_content.decode())

        entry = next((item for item in info_list if item["name"] == Name), None)
        if entry:
            zip_path = entry["path"]
            local_zip_path = os.path.join(download_dir, os.path.basename(zip_path))
            GHFiles(repo_name, zip_path, local_zip_path)
            if zipfile.is_zipfile(local_zip_path):
                Unzip(local_zip_path, download_dir)
                os.remove(local_zip_path)
            else:
                print(f"Error: {local_zip_path} is not a valid zip file.")
        else:
            print(f"No mod found with name '{Name}'")
        ApplyMarketplaceMods(download_dir)