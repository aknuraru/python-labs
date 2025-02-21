import re
def camel_to_snake(camel_case_str):
    snake_case_str = re.sub(r'(?<!^)([A-Z])', r'_\1', camel_case_str)
    return snake_case_str.lower()
camel_case_string = input("Enter a camelCase or PascalCase string: ")
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case:", snake_case_string)
