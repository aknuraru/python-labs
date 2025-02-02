def histogram(lst):
    for num in lst:
        print('*' * num)
user_input = input("numbers separated by spaces: ")
numbers = list(map(int, user_input.split())) 
histogram(numbers)
