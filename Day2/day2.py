def partOne():

    # loops through input, stores, each item(3chars) is new round
    with open('day2.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    # looping through rounds to get total
    totalScore = 0
    for item in data:
        # ROCK
        if item[2] == "X":
            totalScore += 1
            # DRAW
            if item[0] == "A":
                totalScore += 3
            # LOSE
            elif item[0] == "B":
                pass
            # WIN
            elif item[0] == "C":
                totalScore += 6
        # PAPER
        elif item[2] == "Y":
            totalScore += 2
            # WIN
            if item[0] == "A":
                totalScore += 6
            # DRAW
            elif item[0] == "B":
                totalScore += 3
            # LOSE
            elif item[0] == "C":
                pass
        # SCISSORS
        elif item[2] == "Z":
            totalScore += 3
            # LOSE
            if item[0] == "A":
                pass
            # WIN
            elif item[0] == "B":
                totalScore += 6
            # DRAW
            elif item[0] == "C":
                totalScore += 3

    print(totalScore)

def partTwo():

    with open('day2.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    totalScore = 0
    for item in data:
        # LOSE
        if item[2] == "X":
            if item[0] == "A":
                totalScore += 3
            elif item[0] == "B":
                totalScore += 1
            elif item[0] == "C":
                totalScore += 2
        # DRAW
        elif item[2] == "Y":
            totalScore += 3
            # Adds value for choice
            if item[0] == "A":
                totalScore += 1
            elif item[0] == "B":
                totalScore += 2
            elif item[0] == "C":
                totalScore += 3
        # WIN
        elif item[2] == "Z":
            totalScore += 6
            if item[0] == "A":
                totalScore += 2
            elif item[0] == "B":
                totalScore += 3
            elif item[0] == "C":
                totalScore += 1

    print(totalScore)

partTwo()