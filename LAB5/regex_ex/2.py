import re
string=input("input:")
pattern=r'a(bb){2,3}'
if re.search(pattern,string):
    print("Match found")
else:
    print("Match not found")