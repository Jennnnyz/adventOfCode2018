
# coding: utf-8

# In[74]:


import re
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, vx, vy):
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)
        
    def move(self,t):
        self.x += self.vx*t
        self.y += self.vy*t
    
points = []

with open('day10input.txt') as f:
    for line in f:
        stripped = line.rstrip()
        matched = re.findall(r'([-]?[0-9]+)+', stripped)
        p = Point(matched[0], matched[1], matched[2], matched[3])
        points.append(p)
        
        
def have_closely_aligned(points):
    d = {}
    for point in points:
        if point.x in d:
            d[point.x].append(point.y)
        else:
            d[point.x] = []
    for key in d:
        if(len(d[key]) > 6):
            sort = sorted(d[key])
            if(sort[0]+1 == sort[1]):
                return True
    return False

def plot_points(points):
    plt.plot([p.x for p in points], [p.y for p in points],'ro')
    plt.show()

for i in range(20000):
    for point in points:
        point.move(1)
    if(have_closely_aligned(points)):
        print("have closely points @" + str(i))
        plot_points(points)
        
        

