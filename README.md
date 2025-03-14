# file-handling-and-exception-handling
# README

## Description

This project contains a Python script that reads the content of a specified file, modifies the content by converting all text to uppercase, and saves the modified content to a new file. The new file is named by prefixing "modified_" to the original filename.

## Usage

1. The user is prompted to enter the filename of the file to read.
2. The script reads the content of the specified file.
3. The content is modified by converting all text to uppercase.
4. The modified content is saved to a new file with the prefix "modified_" added to the original filename.
5. The script prints a message indicating the name of the modified file.

## How to Run

1. Ensure you have Python installed on your system.
2. Save the code in a file named practice.py.
3. Open a terminal and navigate to the directory containing practice.py.
4. Run the script using the command:
   ```bash
   file_handling.py
   ```
5. Follow the prompts to enter the filename of the file to read.

## Notes

- The script handles `FileNotFoundError` if the specified file does not exist.
- The script handles `IOError` if the file cannot be read.
