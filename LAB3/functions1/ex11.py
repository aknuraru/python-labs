def is_palindrome(text):
    return text == text[::-1]
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

"""
def is_palindrome(text):
    clean_text = "".join(text.lower().split())
    return clean_text == clean_text[::-1]
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

"""
