# This test suite is designed to cover the basic operations of the file organization script.
# It includes tests for directory access, file manipulation, and configuration loading.

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

# Use a dictionary to simulate file type to folder mapping data for testing.
mock_mapping_data = {"txt": "Text Files", "jpg": "Images", "png": "Images"}

def test_get_directory():
    # Simulate incorrect command-line argument to ensure the program exits with an error.
    sys.argv = ["script_name", "wrong_directory"]
    with pytest.raises(SystemExit) as args_error:
        get_directory()
    assert args_error.type == SystemExit
    assert args_error.value.code == 1

def test_load_extension_mapping():
    # Create a temporary json file to simulate the loading of configuration mapping.
    with open("temp.json", "w") as f:
        json.dump(mock_mapping_data, f)
    
    # Load the mapping and verify if it matches the mock mapping data.
    mapping = load_extension_mapping("temp.json")
    assert mapping == mock_mapping_data
    
    # Clean up by deleting the temporary json file.
    os.remove("temp.json")

def test_get_current_directory():
    # Verify that the current directory retrieval function returns a string.
    current_dir = get_current_directory()
    assert isinstance(current_dir, str)

def test_get_files_in_directory():
    # Check if retrieving files from the current directory returns a list.
    files = get_files_in_directory(".")
    assert isinstance(files, list)

def test_create_folder_if_absent():
    # Set up a temporary folder name to test folder creation.
    temp_folder_name = "test_temp_folder"
    # Pre-check to ensure the folder does not exist before testing.
    if os.path.exists(temp_folder_name):
        os.rmdir(temp_folder_name)
    
    # Execute function to potentially create the folder.
    create_folder_if_absent(temp_folder_name)
    # Verify if the folder has been created successfully.
    assert os.path.exists(temp_folder_name)
    
    # Clean up by removing the folder after the test.
    os.rmdir(temp_folder_name)

def test_move_file_to_folder():
    # Prepare a testing environment by setting up source and destination folders and a test file.
    source_folder = "test_source_folder"
    destination_folder = "test_destination_folder"
    test_file_name = "test_file.txt"
    
    # Ensure source and destination folders are created.
    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(destination_folder, exist_ok=True)
    
    # Create a test file with some content.
    with open(os.path.join(source_folder, test_file_name), "w") as f:
        f.write("Test content")
    
    # Verify the file exists in the source folder but not yet in the destination.
    assert os.path.isfile(os.path.join(source_folder, test_file_name))
    assert not os.path.isfile(os.path.join(destination_folder, test_file_name))
    
    # Execute the file move operation.
    move_file_to_folder(test_file_name, source_folder, destination_folder)
    
    # Confirm the file has been moved to the destination folder.
    assert not os.path.isfile(os.path.join(source_folder, test_file_name))
    assert os.path.isfile(os.path.join(destination_folder, test_file_name))
    
    # Remove test artifacts after the test
