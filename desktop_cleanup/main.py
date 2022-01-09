"""
Desktop Cleanup script - A QOL Script
"""
import filetype
import tempfile
import os


def main():
    """Run the desktop cleaning script."""
    in_file = "../user_desktop.txt"
    with open(in_file, 'r') as in_file:
        if in_file.read() == "":
            new_desktop_path = input("enter desktop path:\n> ")
            set_desktop_path(in_file, new_desktop_path)
        in_file.seek(0)  # Reset position to start
        desktop_path = str(in_file.read())
        desktop_items = get_desktop_items(desktop_path)


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
