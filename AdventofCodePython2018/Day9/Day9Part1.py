#### Input data is just a sentence
####
#### 429 players
#### last marble is worth 70901 points ie 70901 is number of marbles

#### Rules
#### place 0 marbel first
#### 
#### 

from collections import deque  ##this allows the use of double ended array ie the circle
players = 429
lastmarble = 70901
circle = deque([0])


for marble in range(1,lastmarble + 1):

    if marble % 23 == 0:
        circle.rotate(-7)
        scores[marble % max_players] += marble + circle.pop()
        cirle.rotate(-1)