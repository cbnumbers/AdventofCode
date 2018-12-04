#### make array of both x coordinate and y coordinate
#### make array of both X size and Y size
#### loop through coordinate array, for each coordinate make empty list to loop through i = 0:size and add +1 to each entry in the array
#### should result in two arrays of x and y coverage for each claim
#### then combine covered x and y coordinates and count, then total ea that is >1 this will be answer

import re

inputdata = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\Day3\\Day3Input.txt", "r").read()

print(inputdata)

clean_claims = ''

clean_claims = re.sub(r'(.* @ |:)','',inputdata).split()
print(clean_claims)

co = []
size = [] 

for x in range(len(clean_claims)):
    if x % 2 == 0:
        co.append(clean_claims[x])
    else:
        size.append(clean_claims[x])

print(co[0:20])
size[0:20]  
s = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\Day3\\size.txt", "w")
s.write(str(size[0]))
s.close



