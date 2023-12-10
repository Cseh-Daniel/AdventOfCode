f = open('input.txt', 'r')
lines = f.readlines()

maxAmount = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for l in lines:
    l = l[l.index(":") + 2:len(l)]
    l = l.split(";")

    for i,j in l:
        l[i]=j.split(",")

    print(l)
