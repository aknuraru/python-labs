from functools import reduce
def multiply(numbers):
    return reduce(lambda x, y: x*y, numbers)
my_list = [1, 2, 3, 4]
result = multiply(my_list)
print(result)  
