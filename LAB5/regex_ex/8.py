import re
text=input()
split_text=re.findall('[A-Z][^A-Z]*',text)
print(split_text)

