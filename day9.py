
# coding: utf-8

# In[78]:


import re
from itertools import cycle
import numpy as np

with open('day9input.txt') as f:
    content = f.read().rstrip()
    match = re.match(r'(.*) players; last marble is worth (.*) points', content)
    num_of_players, highest_pt = int(match.group(1)), int(match.group(2))
    
print("highest: " + str(highest_pt))
print("num_of_players: " + str(num_of_players))



# In[68]:


#part I

players = np.zeros(num_of_players)
marbles = list([0,1])
current_index = 1
current_player = 1
turns = 2

def get_cycle_index(start, count, isClockwise):    
    if(not isClockwise):
        start -= count
    else:
        start += count
    start = start % len(marbles)
    return start
            
def place(start,num):
    if(num % 23 == 0):
        players[current_player] += num
        index = get_cycle_index(start, 7, False)
        players[current_player] += marbles.pop(index)
        return (index % len(marbles))
    else:
        index = get_cycle_index(start,1,True)
        marbles.insert(index+1, num)
        return index+1
    
while(turns <= highest_pt):
    current_player = turns % num_of_players;
    current_index = place(current_index,turns)
    turns += 1

print(players.max())


# In[79]:


#part II
players = np.zeros(num_of_players)

class Marble:
    def __init__(self, value, nxt, pre):
        self.value = value
        self.nxt = nxt
        self.pre = pre
        
    def print(self):
        print("my value is " + str(self.value))
        print("my next is " + str(self.nxt.value))
        print("my previous is " + str(self.pre.value))
        print("--------")
    def printl(self, count):
        m = self
        for i in range(count):
            print(m.value)
            m = m.nxt

marble0 = Marble(0, None, None)
marble0.nxt = marble0
marble0.pre = marble0

marble1 = Marble(1, marble0, marble0)
marble0.nxt = marble1
marble0.pre = marble1
current_marble = marble1
current_player = 1
turns = 2

def get_cycle_marble(marble, count, isClockwise):
    temp = marble
    if(not isClockwise):
        for i in range(count):
            temp = temp.pre
    else:
        for i in range(count):
            temp = temp.nxt
    return temp
            
def place(marble, num):
    if(num % 23 == 0):
        players[current_player] += num
        next_marble = get_cycle_marble(marble, 7, False)
        players[current_player] += next_marble.value
        next_marble.nxt.pre = next_marble.pre
        next_marble.pre.nxt = next_marble.nxt
        marble = next_marble.nxt
        return marble
    else:
        next_marble = get_cycle_marble(marble,1,True)
        marble = Marble(num, next_marble.nxt, next_marble)
        marble.pre.nxt = marble
        marble.nxt.pre = marble
        return marble
highest_pt *= 100    
while(turns <= highest_pt):
    current_player = turns % num_of_players;
    current_marble = place(current_marble, turns)
    turns += 1

print('answer: ' + str(int(players.max())))

