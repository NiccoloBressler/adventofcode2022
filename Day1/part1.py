# loop through input, every line break is a new elf, store total, compare to next value
with open('part1.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

highestCalories = 0
counter = 0
for item in data:
    # If line has a value
    if item != "":
        counter += int(item)
    # If line is blank
    else:
        if counter > highestCalories:
            highestCalories = counter   
        counter = 0

print(highestCalories)
