def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())
    return string == string[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "it is not a palindrome")