input_text = open("input.txt", "r").read()
input_list = input_text.split("\n")
a = "rock"
b = "paper"
c = "scissors"

x = "rock"
y = "paper"
z = "scissors"

score = """
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
points = 0
for i in input_list:
    if i == "A X":
        points = points + 4
    elif i == "A Y":
        points = points + 8
    elif i == "A Z":
        points = points + 3
    elif i == "B X":
        points = points + 1
    elif i == "B Y":
        points = points + 5
    elif i == "B Z":
        points = points + 9
    elif i == "C X":
        points = points + 7
    elif i == "C Y":
        points = points + 2
    elif i == "C Z":
        points = points + 6
print(f"Total points: {points}")

a = "rock"
b = "paper"
c = "scissors"

x = "lose"
y = "draw"
z = "win"

points = 0
for i in input_list:
    if i == "A X":
        points = points + 3
    elif i == "A Y":
        points = points + 4
    elif i == "A Z":
        points = points + 8
    elif i == "B X":
        points = points + 1
    elif i == "B Y":
        points = points + 5
    elif i == "B Z":
        points = points + 9
    elif i == "C X":
        points = points + 2
    elif i == "C Y":
        points = points + 6
    elif i == "C Z":
        points = points + 7
print(f"Total points according to strategy guide: {points}")
