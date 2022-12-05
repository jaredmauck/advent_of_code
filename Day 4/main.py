with open("input.txt", "r") as input:
    input_text_file = input.read()

input_format = input_text_file.replace(",", "\n")
input_text = input_format.replace("-", "\n")

input_list = input_text.split("\n")
firstpart = []
secondpart = []
x = 0
for n, item in enumerate(input_list):
    if n == 0 + x:
        firstpart.append(int(item))
        x = x + 2
    else:
        secondpart.append(int(item))
final_list = []
for y, z in zip(firstpart, secondpart):
    for i in range(y, z + 1):
        final_list.append(i)
print(final_list)
    





