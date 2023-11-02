
---

# File Organizer

**File Organizer** is a tool designed to simplify the process of tidying up your files. It categorizes and moves files into folders based on their extensions, guided by a customizable mapping defined in a JSON configuration file.

## Features

- **Configurable Mapping**: Adapt the file organization logic by editing `file_types.json`.
- **CLI Friendly**: Run the script from the command line for easy automation.
- **Dynamic Directory Support**: Target any directory for file organization or use the current one by default.
- **Safe File Handling**: Avoids overwriting by renaming duplicate files.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system to execute the script. You can download Python from [python.org](https://www.python.org/downloads/).

### Setup

1. Clone the repository or download the script and `file_types.json`.
2. Modify `file_types.json` to define your preferred folder mappings for file extensions.

## How It Works

### Step-by-Step Operations

1. **Target Directory Identification**: `get_directory()`
   - Utilizes a command-line argument for the target directory, with a fallback to the current directory if none is provided.
   - Robust error handling for incorrect or excessive input.

2. **Extension-Folder Mapping**: `load_extension_mapping(json_file)`
   - Loads the mapping rules from a JSON file that associate file extensions with destination folders.

3. **File Discovery**: `get_files_in_directory(directory)`
   - Enumerates files in the target directory, preparing them for organization.

4. **File Organization**: `organize_files(files, directory, extension_mapping)`
   - Determines appropriate folders for files based on their extensions and moves them accordingly.
   - Creates destination folders on-the-fly if they don't already exist.

### Auxiliary Functions

- `create_folder_if_absent(folder_path)`: Ensures the existence of the destination folders.
- `move_file_to_folder(file, source_folder, destination_folder)`: Relocates files, renaming duplicates to prevent data loss.

## How to Use

Run the script via the command line, specifying the path to the directory you wish to organize:

```bash
$ python project.py [directory_path]
```

If `[directory_path]` is omitted, the script organizes files in the script's current directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Any contributions are **greatly appreciated**.

---

