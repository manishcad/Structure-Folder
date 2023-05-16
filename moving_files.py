import os
import shutil

def create_folder(path):
    """Create a folder if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def move_files_by_extension(source_dir, destination_dir):
    """Move files by extension to respective folders"""
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            destination_path = os.path.join(destination_dir, file_extension[1:].lower())
            create_folder(destination_path)
            source_path = os.path.join(root, file)
            try:
                shutil.move(source_path, destination_path)
            except:
                pass
# Pass Your Full Directory Name For SOurce and For destination
source_directory = r"C:\Users\manis\Downloads"
destination_directory = r"C:\Users\manis\Downloads"

move_files_by_extension(source_directory, destination_directory)
print("Done")