'''
file = open("day2.txt")
directions = {
    "forward" : ["hor", 1],
    "down" : ["ver", 1],
    "up" : ["ver", -1]
}
position = {
    "ver" : 0,
    "hor" : 0
}

for line in file:
    line = line.rstrip() # removing newlines
    # splitting lines into the direction string and the movement integer
    axis = directions[line.split()[0]]
    value = int(line.split()[1])
    position[axis[0]] += axis[1] * value

print("First problem solution: ", position["ver"]*position["hor"])
'''

file = open("day2.txt")
directions = {
    "down" : ["aim", 1],
    "up" : ["aim", -1]
}
position = {
    "ver" : 0,
    "hor" : 0,
    "aim" : 0
}

for line in file:
    line = line.rstrip() # removing newlines
    # splitting lines into the direction string and the movement integer
    axis = line.split()[0]
    value = int(line.split()[1])
    if axis != "forward":
        position["aim"] += value * directions[axis][1]
    else:
        position["hor"] += value
        position["ver"] += position["aim"] * value

    print(position)
print(position)
print("Second problem solution: ", position["ver"]*position["hor"])
