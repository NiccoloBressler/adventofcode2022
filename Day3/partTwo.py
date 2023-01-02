def partTwo():

    with open('part1.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    priority_bank = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0

    for sack in data[:-2:3]:
        second_sack = data[data.index(sack)+1]
        third_sack = data[data.index(sack)+2]

        for item in sack:
            if item in second_sack and item in third_sack:
                sum += priority_bank.index(item) + 1
                break

    return sum

print(partTwo())

