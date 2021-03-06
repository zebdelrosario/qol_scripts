"""
Desktop Cleanup script - A QOL Script
"""
import tempfile
import os
import shutil
from pathlib import Path


def main():
    """Run the desktop cleaning script."""
    file_extension_for_file_type = {"image": ["jpg", "jpeg", "png", "bmp", "gif", "psd"],
                                    "video": ["mp4", "avi", "wmv", "mov", "flv", "dv"],
                                    "audio": ["mp3", "aiff", "wav", "wma", "aac", "ra"],
                                    "pdf": ["pdf"],
                                    "microsoft office": ["doc", "docx", "xlsx", "xlsm", "xlsb"],
                                    "Shortcuts": ["url", "lnk"],
                                    "Executables": ["exe"]
                                    }
    in_file = "../user_desktop.txt"
    with open(in_file, 'r') as in_file:
        if in_file.read() == "":
            new_desktop_path = input("enter desktop path:\n> ")
            set_desktop_path(in_file, new_desktop_path)
        in_file.seek(0)  # Reset position to start
        desktop_path = str(in_file.read())
        desktop_items = get_desktop_items(desktop_path)
        create_directories(file_extension_for_file_type, desktop_path)
        for desktop_item in desktop_items:
            desktop_item_path = desktop_path + "\\" + desktop_item
            file_extension = os.path.splitext(desktop_item)
            key = find_key(file_extension_for_file_type, str(file_extension[1]).lower())
            if key is not None:
                shutil.move(desktop_item_path, desktop_path + "\\" + key)
                print(f'{desktop_item_path:<25} has been moved to {desktop_path}\\{key}.')
            elif os.path.isdir(desktop_item_path):
                print(f"{desktop_item_path} is a folder, WILL NOT MOVE.")
            else:
                shutil.move(desktop_item_path, desktop_path + "\\" + "other")
                print(f'{desktop_item:<25} has been moved to {desktop_path}\\other.')


def create_directories(input_dict, current_directory):
    """Create directories for every key of a dictionary."""
    new_directories = [k for k in input_dict.keys()]
    for item in new_directories:
        path = Path(current_directory + "\\" + item)
        if not path.exists():
            os.mkdir(str(item))
        else:
            print(f"Folder {item.upper():<16} already exists; ignoring...")
    other = current_directory + '\\' + 'other'
    path = Path(other)
    if not path.exists():
        os.mkdir("other")
    return new_directories


def find_key(input_dict, input_value):
    """Find key of a given dictionary using a value."""
    for key, value in input_dict.items():
        if isinstance(value, list) and input_value[1:] in value:
            return key


def get_desktop_items(desktop_path):
    """Return a list of objects from the desktop path."""
    os.chdir(desktop_path)
    cwd = os.getcwd()
    desktop_items = os.listdir(cwd)
    return desktop_items


def set_desktop_path(source_path, destination_path):
    """Save desktop path to .txt file."""
    temp_file = tempfile.NamedTemporaryFile(mode="r+")
    # Copy in_file to temporary file
    with open(source_path, 'r') as in_file:
        for line in in_file:
            temp_file.write(line.rstrip() + "\n")
    temp_file.seek(0)
    temp_file.write(destination_path)
    # Write modified contents from temporary file to out_file
    with open(source_path, 'w') as out_file:
        for line in temp_file:
            out_file.write(line)
    temp_file.close()


main()
