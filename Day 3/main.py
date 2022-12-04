with open("input.txt", "r") as input:
    input_text = input.read()
input_list = input_text.split("\n")

# duplicates for every rucksack
duplicates = []
for x in input_list:
    firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
    for duplicate1 in firstpart:
            for duplicate2 in secondpart:
                if duplicate1 == duplicate2:
                    duplicates.append(duplicate1)
                    break
            else:
                continue
            break
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
total = 0
for duplicate in duplicates:
    if duplicate.isupper():
        for integer, string in enumerate(alphabet_list):
            if duplicate.lower() == string:
                total = total + integer + 1 + 26
    else:
        for integer, string in enumerate(alphabet_list):
            if duplicate == string:
                total = total + integer + 1
print(f"Total for Duplicates in Rucksack: {total}")

# Badge for every three elves
group_by_three = []
for i in range(0, len(input_list), 3):
    group_by_three.append(input_list[i:i+3])
x = 0
y = 0
badges = []
for item in group_by_three:
    for item in group_by_three[x][y]:
        if item in group_by_three[x][y+1] and item in group_by_three[x][y+2]:
            badges.append(item)
            x = x + 1
            break
total = 0
for badge in badges:
    if badge.isupper():
        for integer, string in enumerate(alphabet_list):
            if badge.lower() == string:
                total = total + integer + 1 + 26
    else:
        for integer, string in enumerate(alphabet_list):
            if badge == string:
                total = total + integer + 1
print(f"Total for Badges every Three Elves: {total}")