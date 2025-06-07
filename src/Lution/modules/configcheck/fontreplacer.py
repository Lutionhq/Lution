import os
import shutil

def Replace(source_file_path, target_folder_path):
    """
    Replaces the content of each file in a target folder with the content of a source file.
    The original filenames in the target folder are preserved.

    Args:
        source_file_path (str): The full path to the source file (e.g., your "font.ttf").
        target_folder_path (str): The full path to the target folder (e.g., the folder with "font_a.ttf").
    """
    if not os.path.isfile(source_file_path):
        print(f"Error: Source file '{source_file_path}' not found.")
        return

    if not os.path.isdir(target_folder_path):
        print(f"Error: Target folder '{target_folder_path}' not found.")
        return
    replaced_count = 0
    error_count = 0

    for filename in os.listdir(target_folder_path):
        target_file_path = os.path.join(target_folder_path, filename)

        if os.path.isfile(target_file_path):
            try:
                shutil.copyfile(source_file_path, target_file_path)
                print(f"Successfully replaced content of: {target_file_path} with content from {source_file_path}")
                replaced_count += 1
            except Exception as e:
                print(f"Error replacing content of '{target_file_path}': {e}")
                error_count += 1
                continue
        else:
            print(f"Skipping (not a file): {target_file_path}") 

