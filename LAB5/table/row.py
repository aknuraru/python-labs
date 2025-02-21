import re
import csv

result = [["Order", "Name", "Total"]]

file = open('row.txt', 'r', encoding = 'utf-8')

text = file.read()

ItemPatternText = r"\n(?P<Order>.*)\n(?P<Name>.*)\n(?P<Count>.*)x(?P<Price>.*)\n(?P<Subtotal>.*)\nСтоимость\n(?P<Total>.*)"

pattern = r"\n(?P<Order>.*)\n(?P<Name>.*)\n(?P<Count>.*)x(?P<Price>.*)\n(?P<Subtotal>.*)\nСтоимость\n(?P<Total>.*)"
compiled_pattern = re.compile(pattern)

items = re.finditer(compiled_pattern, text)

for match in items:
    row = [match.group("Order"), match.group("Name"), match.group("Total")]
    result.append(row)

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)