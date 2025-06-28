import requests
import zipfile
import os

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

def getLog(logNumber):
    logUrl = f"https://logs.tf/logs/log_{logNumber}.log.zip"
    zipName = f"log_{logNumber}.log.zip"
    logFile = f"log_{logNumber}.log"

    response = requests.get(logUrl)
    if response.status_code != 200:
        print("Failed to download the log file. Check the log number.")
        return

    with open(zipName, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(zipName, 'r') as zipRef:
        zipRef.extractall()

    roundWins(logFile)

    os.remove(zipName)
    os.remove(logFile)
