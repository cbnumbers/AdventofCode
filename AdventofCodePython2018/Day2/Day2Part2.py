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
    newsequence.append(''.join(sorted(inputdata[i])))

##create double and triple variables to use as count
double = 0
triple = 0

for n in range(len(newsequence)):
    twodseq = list(newsequence[n])
    
    istwo = 0
    for x in range(len(twodseq)):
        if newsequence[n].count(twodseq[x]) == 2:
            istwo = 1
            double = double + 1

        if istwo == 1:
            break

print(double)

for n in range(len(newsequence)):
    twodseq = list(newsequence[n])
    isthree = 0
    for x in range(len(twodseq)-2):
        if newsequence[n].count(twodseq[x]) == 3:
            isthree = 1
            triple = triple + 1

        if isthree == 1:
            break
print(triple)

print(double * triple)










resultlist = []
cycles = 0

while resultlist.count(frequency) != 2:
    cycles = cycles + 1
    print(cycles)
    for n in range(len(newsequence)):
        frequency = frequency + newsequence[n]
        resultlist.append(frequency)
        if resultlist.count(frequency) == 2:
            print("Calibration frequency is " + str(frequency))
            break
        

        




         



