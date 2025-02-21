import re
string=input().strip()
pattern=r'[A-Z][a-z]+'
matches=re.findall(pattern,string)
print(matches)