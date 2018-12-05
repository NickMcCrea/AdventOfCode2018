

#load Problem1.txt
with open("Input/Problem2.txt") as f:
    content = f.readlines()

freq_counter = dict()

twoCount = 0
threeCount = 0


for line in content:
    chars = list(line)
    letterCount = dict()
    for char in chars:
        if not letterCount.__contains__(char):
            letterCount.update({char:1})
        else:
            newCount = letterCount.get(char) +1
            print(char + " encountered again " + str(newCount))
            letterCount.update({char:newCount})

    twoFlag = False
    threeFlag = False
    for char in letterCount:
        if letterCount.get(char) == 2:
            if not twoFlag: 
                twoCount+=1
            twoFlag = True
        if letterCount.get(char) == 3:
            if not threeFlag:
                threeCount+=1
            threeFlag = True
           
    
print(twoCount * threeCount)