
def roundWins(filePath):
    redRounds = 0
    blueRounds = 0

    with open(filePath, 'r', errors='ignore') as logFile:
        for line in logFile:
            if 'World triggered "Round_Win"' in line:
                if '(winner "Red")' in line:
                    redRounds += 1
                elif '(winner "Blue")' in line:
                    blueRounds += 1

    print(f"Red won {redRounds} rounds")
    print(f"Blue won {blueRounds} rounds")

    if redRounds > blueRounds:
        print("Red won")
    elif blueRounds > redRounds:
        print("Blue won")
    else:
        print("tie")

