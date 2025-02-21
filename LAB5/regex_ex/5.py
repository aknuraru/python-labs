import re
string=input().split()
pattern=r'a.*b$'
for word in string:
    if re.match(pattern,word):
        print(f"{string} matches the pattern")
    else:
        print(f"{string} not matches the pattern")