import re

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"

new_text = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(new_text)