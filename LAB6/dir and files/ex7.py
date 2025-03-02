# Open the source file in read mode
with open("my_list.txt", "r") as source_file:
    # Read the contents of the source file
    contents = source_file.read()

# Open the destination file in write mode
with open("destination.txt", "w") as destination_file:
    # Write the contents to the destination file
    destination_file.write(contents)