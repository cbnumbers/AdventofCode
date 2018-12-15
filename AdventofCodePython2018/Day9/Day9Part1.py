#### Input data is just a sentence
####
#### 429 players
#### last marble is worth 70901 points ie 70901 is number of marbles
#### Part 2 is same solution/problem but with 100 times the amount of players

#### Rules
#### place 0 marbel first
#### 
#### 
#### 

from collections import deque  ##this allows the use of double ended array ie the circle
test = deque([0])

players = 429
lastmarble = 70901 ##7090100
circle = deque([0])
scores = []
c = 0



while c < players:
    scores.append(0)
    c = c + 1


for marble in range(1,lastmarble + 1):

    if marble % 23 == 0:
                
        circle.rotate(7)
        
        scores[marble % players] = scores[marble % players] + marble + circle[0]
        circle.popleft()  ###change this to silent echo and will run much faster
        
    else:
        circle.rotate(-2)
        circle.insert(0,marble)
    
print(max(scores))
