my_list = ["apple", "banana", "cherry", "date"]

# Open a file in write mode
with open("my_list.txt", "w") as file:
    # Loop through the list and write each string to a new line in the file
    for item in my_list:
        file.write(item + "\n")