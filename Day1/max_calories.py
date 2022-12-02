f = open("input.txt", "r")
food_calories = f.readlines()

max_calories = 0
inventory = 0
for calorie in food_calories:
    if calorie == '\n':
        if inventory > max_calories: max_calories = inventory
        inventory = 0
    else:
        inventory += int(calorie)

print(max_calories)
