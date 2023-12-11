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

games = []

for gameId, l in enumerate(lines):
   
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
    sum=sum+(values[0]*values[1]*values[2])
    # print(f"{values} - {sum}")
print(f"the sum of the powers:{sum}")
