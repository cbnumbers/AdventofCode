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

lowerbound = 10762
x = 0
while x < 26:
    
    react = inputlist
    react = re.sub(upperletters[x],'', react)
    react = re.sub(lowerletters[x],'', react)

    finalcheck = 0
    ## fully react loop process
    while finalcheck == 0:
        startlen = len(react)
        for combo in lettercombos:
                react = re.sub(combo,'',react)
        endlen = len(react)
        if startlen == endlen:
            finalcheck = 1
    x = x + 1

    if len(react) < lowerbound:
        lowerbound = len(react)

print(lowerbound)


    







