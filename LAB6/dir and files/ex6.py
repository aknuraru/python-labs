import string

# Get a string of uppercase letters
letters = string.ascii_uppercase

# Loop through each letter and create a file with that letter as the filename
for letter in letters:
    filename = letter + ".txt"
    with open(filename, "w") as file:
        file.write("This is file " + letter + ".txt")