f = open("input.txt")
base = 0
count = -1
for line in f:
    line = int(line.rstrip())
    if line > base:
        count += 1
    base = line  
print(count)
