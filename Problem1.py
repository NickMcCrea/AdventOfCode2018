

#load Problem1.txt
with open("Input/Problem1.txt") as f:
    content = f.readlines()


frequency = 0
for line in content:
    lineInt = int(line)
    frequency += lineInt
    print(frequency)