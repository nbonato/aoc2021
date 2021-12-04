#first problem
f = open("input.txt")
base = 0
count = -1
for line in f:
    line = int(line.rstrip())
    if line > base:
        count += 1
    base = line  
print("Solution to the first problem: ", count)

#second problem
f = open("input.txt")

array = []
tracker = 0
sumUp = 0
for line in f:
    array.append(int(line.rstrip()))

base = 0
count = -1
for i in range(0, len(array)-2):
    sumUp = sum(array[i:i+3])
    if sumUp > base:
        count += 1
    base = sumUp  

print("Solution to the second problem: ", count)
