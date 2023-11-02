
---

# File Organizer

**File Organizer** organizes files within a directory by categorizing and moving them into folders based on their file extensions. This process is navigated by a customizable mapping detailed in a JSON configuration file.

## 🌟 Features

- **Adaptable Configuration**: Tailor the organization logic to your needs by modifying `file_types.json`.
- **Command Line Support**: Execute the script seamlessly from the command line for efficient automation.
- **Versatile Directory Specification**: Target any desired directory for file organization, or use the current directory by default.
- **Secure File Handling**: Avoid overwriting and data loss by renaming duplicate files during the organization process.

## 🚀 Getting Started

### Prerequisites

- Ensure Python is installed on your system. Download Python from [python.org](https://www.python.org/downloads/).
- **Testing Requirements**: 
  - Install `pytest` to execute the test suite. It can be installed via pip:
    ```bash
    pip install pytest
    ```
  - Alternatively, you can install all necessary dependencies including those for testing from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### Setup

1. Clone the repository or download the `project.py` script and `file_types.json`.
2. Adjust `file_types.json` to customize folder mappings for different file extensions according to your requirements.

## 🛠 How It Works

### Step-by-Step Operations

- **Determining Target Directory**: `get_directory()`
   - Accepts a command-line argument for specifying the target directory, defaulting to the current directory if not provided.

- **Loading Extension-Folder Mappings**: `load_extension_mapping(json_file)`
   - Retrieves file extension-to-folder mapping rules from a specified JSON file.

- **File Discovery**: `get_files_in_directory(directory)`
   - Enumerates and prepares files in the target directory for organization.

- **Organizing Files**: `organize_files(files, directory, extension_mapping)`
   - Categorizes and relocates files into specified folders based on their extensions, and dynamically creates destination folders if necessary.

## 🧪 Testing

To ensure that the File Organizer operates correctly, a series of tests are included in the `tests` directory. Execute these tests using pytest to verify the functionality of various parts of the application.

### Running Tests

Navigate to the root directory of the project, and run the following command:

```bash
pytest tests/
```

This will execute all tests and display their results, allowing for the identification and troubleshooting of potential issues.

## 🤝 Contributions

Contributions are warmly welcomed and greatly appreciated, enhancing the tool’s evolution and functionality.

---
