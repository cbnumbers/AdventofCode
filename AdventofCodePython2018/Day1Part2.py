####Advent of Code Day 1 Part 2
####Load input data
inputdata = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\Day2\\AdventDay1Input.txt", "r").read().split()

#### Create sequence integer array with sequence
newsequence = []
for line in inputdata:
    newsequence.append(int(line))

frequency = 0 #maybe need user input for begining frequency
resultlist = []
cycles = 0


### create while loop to check the count of the current frequency value
### also counts number of cycles it took to find first dupe value
while resultlist.count(frequency) != 2:
    cycles = cycles + 1
    print(cycles)
    for n in range(len(newsequence)):
        frequency = frequency + newsequence[n]
        resultlist.append(frequency)
        if resultlist.count(frequency) == 2:
            print("Calibration frequency is " + str(frequency))
            break
        

        




         



