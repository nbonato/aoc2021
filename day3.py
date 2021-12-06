file = open("day3.txt")
check = []
count = 0
for line in file:
    line = line.rstrip()
    if len(check) < 1:
        check = [0] * len(line)
    for i in range(0, len(line)):
        check[i] += int(line[i])
    count += 1

count = count/2
gamma = ""
epsilon = ""
for i in check:
    if i > count:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Solution to the first problem:", int(gamma, 2) * int(epsilon, 2))  
        
file = open("day3.txt")
total = []

check = []
count = 0
for line in file:
    total.append(line.rstrip())

total2 = total
dioxide = []
oxygen = []

for i in range(0,len(total[0])):
    if len(total) > 1:
        oxygen = []
        top = 0
        for element in total:
            top+=int(element[i])
        if top >= len(total)/2:
            common = 1
        else:
            common = 0
        for element in total:
            if int(element[i]) == common:
                oxygen.append(element)
        total = oxygen
    else:
        break

total = total2
for i in range(0,len(total[0])):
    if len(total) > 1:
        dioxide = []    
        top = 0
        for element in total:
            top+=int(element[i])
        if top >= len(total)/2:
            common = 0
        else:
            common = 1
        for element in total:
            if int(element[i]) == common:
                dioxide.append(element)
        total = dioxide 
    else:
        break

print(int(oxygen[0],2) * int(dioxide[0],2))
      
        

'''
for i, digit in enumerate(gamma):
    print(digit, "pos: ", i)
    for element in total:
        if element[i] == digit:
            total2.append(element)
    print(total2)
    total = total2
    total2 = []
'''
