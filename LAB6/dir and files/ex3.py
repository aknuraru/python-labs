import os

path = "/Users/ryskulaknur/Desktop/python labs/LAB6" 

if os.path.exists(path):
    print("Path exists")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist")