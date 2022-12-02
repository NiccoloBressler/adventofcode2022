# loop through input, every line break is a new elf, store total, compare to next value
with open('part1.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

rankTwo = 0
rankThree = 0

# Gets rank 1
rankOne = 0
counter = 0
for item in data:
    # If line has a value
    if item != "":
        counter += int(item)
    # If line is blank
    else:
        if counter > rankOne:
            rankTwo = rankOne
            rankOne = counter
        elif counter > rankTwo and counter <= rankOne:
            rankTwo = counter
        elif counter > rankThree and counter <= rankTwo:
            rankThree = counter
        counter = 0

print(rankOne+rankTwo+rankThree)