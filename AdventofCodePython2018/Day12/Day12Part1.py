#### Advent of Code Day 12
####
####
####
####
import re
##inputdata = open("D:\\CodeProjects\\PythonStuff\\AdventofCodePython2018\\AdventofCodePython2018\\Day12\\Day12Input.txt", "r").read().split()
initialstate = '#...####.##..####..#.##....##...###.##.#..######..#..#..###..##.#.###.#####.##.#.#.#.##....#..#..#..'
inputdata = open("F:\\Awesome Department\\Contract Pricing\\CodeProjects\\AdventofCode\\AdventofCodePython2018\\Day12\\Day12Input.txt", "r").read()

splitdata = re.sub(' \=\> |\n',',' ,inputdata).split(',')
splitdata.pop(len(splitdata)-1)

print(splitdata)

seq = []
val = []

for x in range(len(splitdata)):
    if x % 2 == 0:
        seq.append(splitdata[x])
    else:
        val.append(splitdata[x])

twod = [ [seq[x], val[x]] for x in range(len(seq)) ]

while n <len(twod):
    for x in range(len(twod)):

        if twod[n][1] == '.':
            del(twod[n])
            n = n + 1
print(twod)       
