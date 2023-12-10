import re

f = open('input.txt', 'r')
lines = f.readlines()

sum = 0
numbers = []
strnmbrs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

print(lines)
for line in lines:
    # for i, strnmbr in enumerate(strnmbrs):
    #
    #     if strnmbr in line[1]:
    #         numbers.append(i + 1)
    #
    for char in line:
        if char.isdigit():
            numbers.append(int(char))

    # linehlp = line.split(numbers)
    nmbrsplit = list(map(lambda x: str(x), numbers))
    # számok concatelése és az alapján beletenni a re splitbe
    # olyat kell kapni hogy ?' "5","4"'?
    print(f"\nnmbrsplit:{nmbrsplit}")
    # print(f"{ re.split(*nmbrsplit,line.strip('\n'))}")

    lngth = int(len(numbers) - 1)
    numbers[0] = (numbers[0] * 10) + numbers[lngth]
    sum = sum + numbers[0]
    print(numbers)
    numbers = []

print(f"{sum} alma")
