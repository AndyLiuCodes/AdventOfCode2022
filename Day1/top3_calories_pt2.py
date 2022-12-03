f = open("input.txt", "r")
food_calories = f.readlines()

inventories = []

current = 0
for calorie in food_calories:
    if calorie == '\n':
        inventories.append(current)
        current = 0
    else:
        current += int(calorie)

total = 0

for _ in range(0,3):
    max_cal = max(inventories)
    total += max_cal

    inventories.remove(max_cal)

print(total)

# Ideally, I think the best solution is to use a min-heap and store
# the top 3 calorie counts. Then when the next set of calories for an elf is computed
# we compare it with the min of the heap, if its bigger, then we remove the min of the heap
# and add the new value to the heap. Then re-sort the heap. At the end, we just sum the values in the heap
