
import re,datetime, date, time
#   load list of integers to sum in for loop
timestamps = open("F:\\Awesome Department\\Contract Pricing\\CodeProjects\\AdventofCode\\AdventofCodePython2018\\Day4\\Day4Input.txt").read()
#   loop through elements of freq_change array and sum together then store each iteration as frequency history to find the first repeat.
clean_time = re.sub('\[', '', timestamps)
clean_time = re.sub(r'\] ', ',',clean_time)
clean_time = re.sub(r'Guard \#', '',clean_time)
clean_time = re.sub(r' begins shift', '',clean_time)
clean_time = re.sub(r'\n', ',',clean_time).split(',')


#print(clean_time)

time = []
action = []
for x in range(len(clean_time)):
    if x % 2 == 0:
        time.append(datetime.datetime.strptime(clean_time[x],"%Y-%m-%d %h:%M")) 
    else:
        action.append(clean_time[x])

twod = [ [time[x], action[x]] for x in range(len(action)) ]
twod = sorted(twod, key=lambda x: x[0])
print(twod)

for n in range(len(twod)):

    datetime.strptime(twod[n][0], ) 

datetime.datetime.strptime(twod[n][0]),"%y-%m-%d %H:%M"