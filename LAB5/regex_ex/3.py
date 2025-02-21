import re
string=input().split(",")
pattern=r'[a-z][_]'
for words in string:
    if re.search(pattern,words):
        print(words)

