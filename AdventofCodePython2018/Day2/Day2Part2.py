####Advent of Code Day 2 Part 1
####
####Load input data
inputdata = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\Day2\\Day2Input.txt", "r").read().split()
print(inputdata)

##First order ea entry of letters in alpha sort
##Then find where 2 of same letter are next to ea other, flag as 2 in an array
##repeat for 3
##take the 3 array and the 2 array count 2's and 3's in ea, then multiply those
#### Create sequence integer array with sequence
newsequence = []

for i in range(len(inputdata)):
    newsequence.append(''.join(inputdata[i]))
print(newsequence)
##create double and triple variables to use as count
double = []
triple = []

for n in range(len(newsequence)):
    twodseq = list(newsequence[n])
    istwo = 0
    for x in range(len(twodseq)):
        if newsequence[n].count(twodseq[x]) == 2:
            istwo = 1
            double.append(twodseq)

        if istwo == 1:
            break

print(double)

for n in range(len(newsequence)):
    twodseq = list(newsequence[n])
    isthree = 0
    for x in range(len(twodseq)-2):
        if newsequence[n].count(twodseq[x]) == 3:
            isthree = 1
            triple.append(twodseq)

        if isthree == 1:
            break
print(triple)

print(len(double) * len(triple))

## End of Day2 Part 1

fulllist = list(inputdata)
print(fulllist)
print(len(fulllist[n]))
##listA = list(fulllist[0])
##print(listA)

for n in range(len(fulllist)):
    listA = list(fulllist[n])


    for i in range(len(fulllist)):
        listB = list(fulllist[i])
        workingcode = ''
        c = 0
        match = 0
        diff = 0
        while c < 26:
            
            if listA[c] != listB[c]:
                diff = diff + 1
                

            else:
                match = match + 1
                workingcode = workingcode + listA[c]
            c = c + 1

        if diff == 1:
                print(diff)
                print(workingcode)
