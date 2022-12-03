input_text = open("input.txt", "r").read()
input_list = input_text.split("\n")


for x in input_list:
    firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
    for number1, duplicate1 in enumerate(firstpart):
            for number2, duplicate2 in enumerate(secondpart):
                if duplicate1 == duplicate2:
                    print(duplicate1)
                    break