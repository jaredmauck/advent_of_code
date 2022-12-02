input_text = open("input.txt", "r").read()
input_list = input_text.split("\n")
result = [[]]
for i in input_list:
    if i == '':
        result.append([])
    else:
        result[-1].append(int(i))
s = []
for summary in result:
    s.append(sum(summary))
s.sort()
print(f"The highest amount of calories carried is: {s[-1]}")

top3 = s[-1] + s[-2] + s[-3]
print(f"The total number of calories in the top 3 is: {top3}")