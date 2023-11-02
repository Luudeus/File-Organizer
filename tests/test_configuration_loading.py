# Test suite for configuration loading function in the project.py script.
# This tests the loading of file extension to folder mappings from a JSON configuration file.

from project import load_extension_mapping
import json
import os
import tempfile
import pytest

def test_load_extension_mapping_matches_expected_data():
    # Create a temporary JSON file with predetermined mapping
    temp_json = tempfile.NamedTemporaryFile(delete=False)
    json.dump({"txt": "Text Files", "jpg": "Images", "png": "Images"}, temp_json)
    temp_json.close()

    # Load the mapping and verify that it matches the data provided
    mapping = load_extension_mapping(temp_json.name)
    assert mapping == {"txt": "Text Files", "jpg": "Images", "png": "Images"}

    # Clean up by removing the temporary file
    os.unlink(temp_json.name)

def test_load_extension_mapping_with_malformed_json():
    # Create a malformed JSON file to test error handling
    temp_json = tempfile.NamedTemporaryFile(delete=False)
    temp_json.write(b"{'not: 'a proper', 'json':}")
    temp_json.close()

    # Verify that loading an invalid JSON file raises the appropriate exception
    with pytest.raises(json.JSONDecodeError):
        _ = load_extension_mapping(temp_json.name)

