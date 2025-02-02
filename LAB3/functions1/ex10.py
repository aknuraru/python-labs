def unique_elements(lst):
    unique_list = []  
    for item in lst:
        if item not in unique_list:  
            unique_list.append(item)
    return unique_list
user_input = input()  
numbers = []
for num in user_input.split():
    if "." in num:  
        numbers.append(float(num))
    else:
        numbers.append(int(num))
print(unique_elements(numbers))
