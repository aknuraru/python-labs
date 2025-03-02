import os

# specify the path to check
path = "/Users/ryskulaknur/Desktop/python labs/LAB6"

# check if the path exists
if os.path.exists(path):
    print("Path exists")
else:
    print("Path does not exist")

# check if the path is readable
if os.access(path, os.R_OK):
    print("Path is readable")
else:
    print("Path is not readable")

# check if the path is writable
if os.access(path, os.W_OK):
    print("Path is writable")
else:
    print("Path is not writable")

# check if the path is executable
if os.access(path, os.X_OK):
    print("Path is executable")
else:
    print("Path is not executable")