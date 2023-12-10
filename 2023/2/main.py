f = open('input.txt', 'r')
lines = f.readlines()

colors = ["red", "green", "blue"]
values = [0, 0, 0]
maxAmount = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum=0
isValid = False
games = []

for gameId, l in enumerate(lines):
    isValid = False
    values = [0, 0, 0]

    l = l[l.index(":") + 2:len(l)]
    lines[gameId] = l.strip("\n").split(";")

    for i, draw in enumerate(lines[gameId]):
        lines[gameId][i] = draw.split(",")
        for j, entry in enumerate(lines[gameId][i]):
            curVal = int(entry.strip(" ").split(" ")[0])
            for colIndex, color in enumerate(colors):
                if color in entry:
                    if values[colIndex] < curVal:
                        values[colIndex] = curVal
    for val in values:
        if maxAmount["red"] >= values[0] and maxAmount["green"] >= values[1] and maxAmount["blue"] >= values[2]:
            isValid = True
    games.append(isValid)

for i, game in enumerate(games):
    if game:
        sum=sum+(i+1)
print(sum)

