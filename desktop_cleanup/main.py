"""
Desktop Cleanup script - A QOL Script
"""
import tempfile
import os
import shutil
from pathlib import Path


def main():
    """Run the desktop cleaning script."""
    file_extension_for_file_type = {"image": ["jpg", "jpeg", "png", "bmp", "gif"],
                                    "video": ["mp4", "avi", "wmv", "mov", "flv", "dv"],
                                    "audio": ["mp3", "aiff", "wav", "wma", "aac", "ra"],
                                    "pdf": ["pdf"],
                                    "microsoft office": ["doc", "docx", "xlsx", "xlsm", "xlsb"],
                                    "Shortcuts": ["url"]
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
            # if key is not None:
                # print(f'{desktop_item:<25} will be moved to {key.upper()}.')
            # else:
                # print(f'{desktop_item:<25} = OTHER')


def create_directories(input_dict, destination_path):
    """Create directories for every key of a dictionary."""
    new_directories = [k for k in input_dict.keys()]
    for item in new_directories:
        path = Path(destination_path)
        if not path.exists():
            os.mkdir(str(item))
        else:
            print(f"Folder {item.upper():<16} already exists; ignoring...")


def find_key(input_dict, input_value):
    """Find key of a given dictionary using a value."""
    for key, value in input_dict.items():
        if input_value[1:] == value:
            return key
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
