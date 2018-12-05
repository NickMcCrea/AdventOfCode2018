


def compareStrings(firstString, secondString):

    if firstString == secondString:
        return False
        
    firstChars = list(firstString)
    secondChars = list(secondString)

    falseMatches = 0
    for i in range(0,len(firstChars)-1):
        letterA = firstChars[i]
        letterB = secondChars[i]
        if letterA == letterB:
           continue
        else:
            falseMatches +=1

    if falseMatches > 1:
        return False
    else:
        print(firstString + " " + secondString)
    



#load Problem1.txt
with open("Input/Problem2.txt") as f:
    content = f.readlines()

freq_counter = dict()




for line in content:
    for line2 in content:
        compareStrings(line,line2)
   
