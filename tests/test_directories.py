# Test suite for functions related to directory handling in the project.py script.

from project import get_directory, get_current_directory
import sys
import pytest
import os


def test_get_directory_with_wrong_path():
    # Simulate command line argument for a non-existent directory
    sys.argv = ["script_name", "non_existent_directory"]
    # Expecting SystemExit exception due to invalid directory argument
    with pytest.raises(SystemExit) as exc_info:
        get_directory()
    # Verify that the script exits with the correct exit code
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1


def test_get_current_directory_type():
    # Ensure the get_current_directory function returns a string
    assert isinstance(get_current_directory(), str)


def test_get_directory_with_correct_path():
    # Provide a correct directory through command line argument and verify it is returned
    sys.argv = ["script_name", os.getcwd()]
    assert get_directory() == os.getcwd()


def test_get_directory_no_arguments():
    # Run get_directory without arguments to check it defaults to current directory
    sys.argv = ["script_name"]
    assert get_directory() == get_current_directory()
