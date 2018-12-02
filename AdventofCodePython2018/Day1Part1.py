####Advent of Code Day 1 Part 1
####Load input data
inputdata = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\AdventDay1Input.txt", "r").read().split()

#### Create integer array with sequence
newsequence = []
for line in inputdata:
    newsequence.append(int(line))

frequency = 0 #maybe need user input for begining frequency

for n in range(len(newsequence)):
    frequency = frequency + newsequence[n]

print(frequency)
print("You sent me to F'n " + str(frequency) + " frequency ya tard")
