"""
This module organizes files based on their extensions using a predefined mapping.
"""

import os
import shutil
import json
import sys


def main():
    """
    Main function to organize files based on their extensions.
    """
    # Retrieve the target directory for file organization
    directory = get_directory()

    # Load the mapping of file extensions to respective folders
    extension_mapping = load_extension_mapping("file_types.json")

    # Enumerate all files within the target directory
    files = get_files_in_directory(directory)

    # Categorize and move files to designated folders
    organize_files(files, directory, extension_mapping)


def get_directory():
    """
    Determine the target directory for file organization.

    If an argument is provided, it's considered as the target directory.
    If no argument is provided, the current working directory is used.
    If more than one argument is provided, an error message is displayed.

    :return: The absolute path of the target directory
    :rtype: str
    """
    # Check if a directory argument was provided
    if len(sys.argv) == 2:
        directory = sys.argv[1]
        if not os.path.isdir(directory):
            print(f"Error: The directory '{directory}' doesn't exist.")
            print("If given correctly, quote the directory using '' or \"\".")
            sys.exit(1)
    # Check if more than two args were given
    elif len(sys.argv) > 2:
        print("Too many arguments. Usage: project.py ['directory'].")
        sys.exit(1)
    # If no arguments were given, use the current working directory
    else:
        directory = get_current_directory()
    return directory


def load_extension_mapping(json_file):
    """
    Load a mapping of file extensions to folder names from a JSON file.

    :param json_file: Path to the JSON file
    :type json_file: str
    :return: Dictionary of file extension to folder name
    :rtype: dict
    """
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def get_current_directory():
    """
    Retrieve the current working directory.

    :return: Absolute path of the current directory
    :rtype: str
    """
    return os.getcwd()


def get_files_in_directory(directory):
    """
    Get all files in a given directory.

    :param directory: Path to the directory
    :return: List of files in the directory
    :rtype: list
    """
    entries = os.listdir(directory)
    files = []

    for entry in entries:
        entry_path = os.path.join(directory, entry)

        # Check if the entry is a file
        if os.path.isfile(entry_path):
            files.append(entry)

    return files


def create_folder_if_absent(folder_path):
    """
    Create a folder if it doesn't exist.

    :param folder_path: Path to the folder
    :type folder_path: str
    :return: None
    :rtype: None
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def move_file_to_folder(file, source_folder, destination_folder):
    """
    Move a file from a source folder to a destination folder.
    If a file with the same name exists in the
    destination folder, rename the incoming file.

    :param file: Name of the file
    :type file: str
    :param source_folder: Path to the source folder
    :type source_folder: str
    :param destination_folder: Path to the destination folder
    :type destination_folder: str
    :return: None
    :rtype: None
    """
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)

    # Check if the file already exists in the destination folder
    counter = 1
    while os.path.exists(destination_path):
        file_name, file_extension = os.path.splitext(file)
        new_file_name = f"{file_name}({counter}){file_extension}"
        destination_path = os.path.join(destination_folder, new_file_name)
        counter += 1

    shutil.move(source_path, destination_path)


def organize_files(files, directory, extension_mapping):
    """
    Organize files into folders based on their extensions.

    :param files: List of the files to be organized
    :type files: list
    :param directory: Directory where the files are located
    :type directory: str
    :param extension_mapping: Mapping of file extensions to folder names
    :type extension_mapping: dict
    :return: None
    :rtype: None
    """
    for file in files:
        if "." in file:
            file_extension = file.split(".")[-1].lower()
        else:
            print(
                f"File name '{file}' doesn't have an extension in its name. Skipping."
            )
            continue
        if file_extension in extension_mapping:
            folder_name = extension_mapping[file_extension]
            folder_path = os.path.join(directory, folder_name)

            create_folder_if_absent(folder_path)
            move_file_to_folder(file, directory, folder_path)

        else:
            print(
                f"File format .{file_extension} in file '{file}' unsupported. Skipping."
            )
            continue


if __name__ == "__main__":
    main()
