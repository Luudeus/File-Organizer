# File Organizer

This script organizes files in a directory based on their file extensions using a predefined mapping from a JSON file.
If needed, feel free to change the contents of `file_types.json`
#### Video Demo: https://youtu.be/qJYWaK0bnv4

## Overview

1. **Initial Configuration**: A predefined JSON file holds the mapping of which file formats belong to which destination folders.
2. **Command Line Execution**: The script can be executed from the command line, potentially taking a directory as an argument.
3. **File Scanning & Organization**: The script scans the given directory (or the directory from which it's run if no argument is given), categorizes files, and moves them to their respective folders as per the JSON configuration.

## Breakdown

### 1. Determining the Target Directory: `get_directory()`

- If a directory is specified as an argument, it's considered as the target.
- If no directory is given, the script uses the directory it's currently in.
- An error is displayed if more than one argument is provided.

### 2. Loading File Extension Mappings: `load_extension_mapping(json_file)`

- This function reads a JSON file and returns a dictionary that maps file extensions to respective folders.

### 3. Retrieving Files: `get_files_in_directory(directory)`

- Returns all files within the specified directory.

### 4. Organizing Files: `organize_files(files, directory, extension_mapping)`

- Goes through each file in the directory.
- For each file, it determines the file extension and then checks the mapping to see where the file should be moved.
- If the destination folder doesn't exist, it's created.
- Files are then moved to their respective folders, and if a file with the same name exists in the destination, the incoming file is renamed to avoid conflicts.

## Utility Functions

- `create_folder_if_absent(folder_path)`: Creates a folder if it doesn't exist.
- `move_file_to_folder(file, source_folder, destination_folder)`: Moves a file from one folder to another, handling the case where a file of the same name already exists in the destination.

## Execution

To execute the script, it can be run from the command line with the option to specify a target directory. If no directory is given, it organizes files in the directory where the script resides.

## Usage
$ python project.py ['directory_path']
