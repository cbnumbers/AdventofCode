#### make array of both x coordinate and y coordinate
#### make array of both X size and Y size
#### loop through coordinate array, for each coordinate make empty list to loop through i = 0:size and add +1 to each entry in the array
#### should result in two arrays of x and y coverage for each claim
#### then combine covered x and y coordinates and count, then total ea that is >1 this will be answer
import re 
inputdata = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\Day5\\Day5Input.txt", "r").read().split()
print(inputdata[0])

inputlist = inputdata[0]

upperletters = []
lowerletters = [
           "a","b","c","d","e","f","g","h","i","j","k",
           "l","m","n","o","p","q","r","s","t","u",
           "v","w","x","y","z"]

for x in range(len(lowerletters)):

    upperletters.append( lowerletters[x].capitalize())
print(upperletters)

lettercombos = []
for y in range(len(lowerletters)):
    lettercombos.append(str(lowerletters[y]) + str(upperletters[y]))
    lettercombos.append(str(upperletters[y]) + str(lowerletters[y]))

print(lettercombos)

finalcheck = 0
react = inputlist

while finalcheck == 0:
    startlen = len(react)
    for combo in lettercombos:
            react = re.sub(combo,'',react)
    endlen = len(react)
    if startlen == endlen:
        finalcheck = 1
print(react)
print(len(react))







