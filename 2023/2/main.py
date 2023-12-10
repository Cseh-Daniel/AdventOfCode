f = open('input copy.txt', 'r')
lines = f.readlines()

colors = ["red", "green", "blue"]
values = [0,0,0]
maxAmount = {
    'red': 12,
    'green': 13,
    'blue': 14
}

isValid=False

for gameId,l in enumerate(lines):
    isValid=False
    values = [0,0,0]
   
    l = l[l.index(":") + 2:len(l)]
    l = l.strip("\n").split(";")

    for i,j in enumerate(l):
        l[i]=j.split(",")
        for idx, lj in enumerate(l[i]):
            l[i][idx]=lj.strip(" ")
            
            for ci,color in enumerate(colors):
                currentVal=int(l[i][idx][0])
                if color in l[i][idx] and currentVal>values[ci]:
                    values[ci]=currentVal
    print(values)
            

    print(f"{gameId+1}{l}\n{gameId+1} {isValid}\n")



for i in colors:
    print(i)