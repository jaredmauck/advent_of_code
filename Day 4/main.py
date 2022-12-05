import re

with open("input.txt", "r") as input:
    input_text_file = input.read()

input_format = input_text_file.replace(",", "\n")
input_text = input_format.replace("-", "\n")

input_list = input_text.split("\n")
# print(input_text)
# formatted_list = []
# for i in input_list:
#     if i == '':
#         formatted_list.append([])
#     else:
#         formatted_list[-1].append(int(i))
firstpart = []
secondpart = []
x = 0
for n, item in enumerate(input_list):
    if n == 0 + x:
        firstpart.append(int(item))
        x = x + 2
    else:
        secondpart.append(int(item))

for y in firstpart, secondpart:
    print(range(y, y))
    





