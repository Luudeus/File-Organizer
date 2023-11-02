# Test suite for file management functions within the project.py script.
# This includes creating directories, moving files, and listing directory contents.

from project import get_files_in_directory, create_folder_if_absent, move_file_to_folder
import os
import tempfile
import pytest

# Using pytest fixtures to setup a clean test environment before each test
@pytest.fixture
def create_test_environment():
    # Setup temporary directories and a file for testing file operations
    source_folder = tempfile.mkdtemp()
    destination_folder = tempfile.mkdtemp()
    test_file_name = "test_file.txt"
    test_file_path = os.path.join(source_folder, test_file_name)
    with open(test_file_path, "w") as f:
        f.write("Test content")
    return source_folder, destination_folder, test_file_name

def test_get_files_in_directory_returns_list(create_test_environment):
    source_folder, _, _ = create_test_environment
    # Ensure that the function returns a list of files
    files = get_files_in_directory(source_folder)
    assert isinstance(files, list)

def test_create_folder_if_absent_creates_folder():
    # Create a temporary directory path for testing folder creation
    temp_folder_path = tempfile.mkdtemp()
    os.rmdir(temp_folder_path)  # Preemptively remove it to test folder creation
    create_folder_if_absent(temp_folder_path)
    # Verify that the directory was created
    assert os.path.isdir(temp_folder_path)
    os.rmdir(temp_folder_path)  # Clean up after test

def test_move_file_to_folder_moves_file(create_test_environment):
    source_folder, destination_folder, test_file_name = create_test_environment
    # Execute the move operation
    move_file_to_folder(test_file_name, source_folder, destination_folder)
    # Verify that the file has been moved from the source to the destination
    assert not os.path.exists(os.path.join(source_folder, test_file_name))
    assert os.path.exists(os.path.join(destination_folder, test_file_name))

# Clean up the temporary directories and files after each test
def teardown_function(function, create_test_environment):
    source_folder, destination_folder, _ = create_test_environment
    if os.path.isdir(source_folder):
        os.rmdir(source_folder)
    if os.path.isdir(destination_folder):
        os.rmdir(destination_folder)
