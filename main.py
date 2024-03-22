import random

i = 1
total_points = 0
points = 0
reroll = False

while (i < 7):
    reroll = False
    if (points >= 21):
        print(f"Round {i} over, you earned {points} points")
        points = 0
        print(f"Your total points is now {total_points}")
        i += 1
        continue


    rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    print(rolls)

    if (rolls[0] == rolls[1]) and (rolls[2] == rolls[0]) and (rolls[0] == i):
        print("Bunko!")
        points += 21
        total_points += 21
        continue
    elif (rolls[0] == rolls[1]) and (rolls[0] == rolls[2]):
        print("Mini-Bunko")
        points += 5
        total_points += 5
        reroll = True

    if (rolls[0] == i):
        points += 1
        total_points += 1
        reroll = True
    if (rolls[1] == i):
        points += 1
        total_points += 1
        reroll = True
    if (rolls[2] == i):
        points += 1
        total_points += 1
        reroll = True


    if (not reroll):
        print(f"Round {i} over, you earned {points} points")
        points = 0
        i += 1
        print(f"Your total points is now {total_points}")

print(f"The game is over and you earned {total_points} points")