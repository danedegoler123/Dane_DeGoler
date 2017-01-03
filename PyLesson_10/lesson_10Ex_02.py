go = input("Enter 16 words: ")
spList = go.split(" ")
wordsList = []

spot = 0
for i in range(0, 4):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(spList[spot])
        output += wordsList[i][j] + "\t"
        if spot < len(spList)-1:
            spot += 1
    print(output)     



