from github import Github as g
from modules.utils.files import ApplyMarketplaceMods, ResetMods2
from modules.configcheck.config import UpdateLutionMarketplaceConfig as cfmk, ReadLutionMarketplaceConfig as rmk
import os
import zipfile
import requests
import json
import time
import urllib
import base64

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
    """Downloads a file from a public GitHub repository using github_file_to_bytes with retry logic."""
    for attempt in range(max_retries):
        try:
            print(f"Attempting to download '{file_path}' from '{repo_name}' (Attempt {attempt + 1}/{max_retries})")
            api_url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
            response = requests.get(api_url)
            response.raise_for_status()
            file_info = response.json()

            if file_info.get('download_url'):
                url = file_info['download_url']
                print(url)
                file_response = requests.get(url)
                file_response.raise_for_status()
                content = file_response.content
            elif file_info.get('content') and file_info.get('encoding') == 'base64':
                content = base64.b64decode(file_info['content'])
            else:
                raise Exception("Unable to retrieve file content from GitHub API.")

            with open(output_path, "wb") as f:
                f.write(content)
            response = requests.get(url)  
            response.raise_for_status() 
            with open(output_path, "wb") as f:
                f.write(response.content)

            print(f"Successfully downloaded '{file_path}' from '{repo_name}' to '{output_path}'")
            return

        except requests.exceptions.RequestException as e:
            print(f"Download failed (Attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Max retries reached. Download failed.")
                raise

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

def DownloadMarketplace(Name, type):
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
                return download_dir
            else:
                print(f"Error: {local_zip_path} is not a valid zip file.")
        else:
            print(f"No theme found with name '{Name}'")
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
                return download_dir
            else:
                print(f"Error: {local_zip_path} is not a valid zip file.")
        else:
            print(f"No mod found with name '{Name}'")
    return None

def ApplyMarketplace(Name, type):
    ResetMods2()
    download_dir = os.path.expanduser(f"~/Documents/Lution/Lution Marketplace/{type}s/{Name}")

    if type == "theme":
        curf = rmk("InstalledThemes")
        if not curf:
            curf = ""
        if Name not in curf:
            cfmk("InstalledThemes", Name + "," + curf if curf else Name)
        ApplyMarketplaceMods(download_dir)
    elif type == "mod":
        curf = rmk("InstalledMods")
        if not curf:
            curf = ""
        if Name not in curf:
            cfmk("InstalledMods", Name + "," + curf if curf else Name)
        ApplyMarketplaceMods(download_dir)