"""
Desktop Cleanup script - A QOL Script
"""
import filetype
import tempfile
import os


def main():
    """Run the desktop cleaning script."""
    desktop_path = "user_desktop.txt"
    with open(desktop_path, 'r') as in_file:
        if in_file.read() == "":
            set_desktop_path(desktop_path)


def set_desktop_path(desktop_path):
    temp_file = tempfile.NamedTemporaryFile(mode="r+")
    # Copy in_file to temporary file
    with open(desktop_path, 'r') as in_file:
        for line in in_file:
            temp_file.write(line.rstrip() + "\n")
    temp_file.seek(0)
    # Write modified contents from temporary file to out_file
    with open(desktop_path, 'w') as out_file:
        for line in temp_file:
            out_file.write(line)
    temp_file.close()


def navigate_to_desktop(desktop_path):
    """Get the current working directory."""
    cwd = os.getcwd()
    os.chdir()


main()
