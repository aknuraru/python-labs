import os

# Corrected absolute path for macOS
path = "/Users/ryskulaknur/Desktop/python labs/LAB2"

# Check if the directory exists before listing contents
if os.path.exists(path) and os.path.isdir(path):
    # List only directories
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    # List only files
    print("Files:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    # List all directories and files
    print("All Directories and Files:")
    for entry in os.listdir(path):
        print(entry)

else:
    print(f"ERROR: The directory '{path}' does not exist.")
