import re
pattern=r'a[b]*'
input_strings=input().split(",")
for string in input_strings:
    string=string.strip()
    match=re.search(pattern,string)
    if match:
        print(f"{string} matched the pattern '{pattern}'")
    else:
        print(f"{string} did not match the pattern '{pattern}'")

