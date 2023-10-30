from project import (
    get_directory,
    load_extension_mapping,
    get_current_directory,
    get_files_in_directory,
    create_folder_if_absent,
    move_file_to_folder,
)
import json
import os
import sys
import pytest

# Mock data for testing
mock_mapping_data = {"txt": "Text Files", "jpg": "Images", "png": "Images"}


def test_get_directory():
    sys.argv = ["script_name", "wrong_directory"]
    with pytest.raises(SystemExit) as args_error:
        get_directory()
    assert args_error.type == SystemExit
    assert args_error.value.code == 1


def test_load_extension_mapping():
    # Save mock_mapping_data to a temporary json file
    with open("temp.json", "w") as f:
        json.dump(mock_mapping_data, f)

    mapping = load_extension_mapping("temp.json")
    assert mapping == mock_mapping_data
    # Delete the temporary json file
    os.remove("temp.json")


def test_get_current_directory():
    current_dir = get_current_directory()
    assert isinstance(current_dir, str)


def test_get_files_in_directory():
    files = get_files_in_directory(".")
    assert isinstance(files, list)


def test_create_folder_if_absent():
    # Define a temporary folder name
    temp_folder_name = "test_temp_folder"
    # Ensure folder doesn't exist at the start
    if os.path.exists(temp_folder_name):
        os.rmdir(temp_folder_name)
    # Call the function to create the folder
    create_folder_if_absent(temp_folder_name)
    # Check if the folder has been created
    assert os.path.exists(temp_folder_name) == True
    # Clean up by removing the created folder
    os.rmdir(temp_folder_name)


def test_move_file_to_folder():
    # Create source and destination folders and a sample file
    source_folder = "test_source_folder"
    destination_folder = "test_destination_folder"
    test_file_name = "test_file.txt"

    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(destination_folder, exist_ok=True)

    with open(os.path.join(source_folder, test_file_name), "w") as f:
        f.write("Test content")

    # Ensure the file exists in the source folder but not in the destination
    assert os.path.exists(os.path.join(source_folder, test_file_name)) == True
    assert os.path.exists(os.path.join(destination_folder, test_file_name)) == False

    # Call the function to move the file
    move_file_to_folder(test_file_name, source_folder, destination_folder)

    # Ensure the file no longer exists in the source folder but exists in the destination
    assert os.path.exists(os.path.join(source_folder, test_file_name)) == False
    assert os.path.exists(os.path.join(destination_folder, test_file_name)) == True

    # Remove the created folders and file
    os.remove(os.path.join(destination_folder, test_file_name))
    os.rmdir(source_folder)
    os.rmdir(destination_folder)
