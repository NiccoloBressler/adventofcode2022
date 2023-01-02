# List of items
def partOne():
    with open('part1.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    priority_bank = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0

    # Loop through items
    for item in data:
        # Split items in half
        firstpart, secondpart = item[:len(item)//2], item[len(item)//2:]
        # Compare halves
        for char in firstpart:
            if char in secondpart:
                sum += priority_bank.index(char) + 1
                break

    # Find sum

    return sum