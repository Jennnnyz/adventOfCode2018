from collections import Counter
import numpy as np

points = {}

with open('day6input.txt') as f:
	counter = 0
	for line in f:
		line = line.rstrip()
		coords = line.split(',')
		#(tag,x,y)
		points[counter] = (int(coords[0]), int(coords[1]))
		counter += 1

def get_distance(p1, p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

#----------part II--------------

def get_total_distance(coords):
    distance = 0
    for key in points:
        distance += get_distance(coords, points[key])
    return distance

counter = 0
for i in range(500):
    for j in range(500):
        if(get_total_distance((i,j)) < 10000):
            counter += 1
            
print(counter)

#----------part I--------------

matrix = np.zeros((500, 500))

#returns tag of the closest point to a given coordinate
def get_closest(coords):
	minimum = 1000
	cnt = Counter()
	for key in points:
		distance = get_distance(coords, points[key])
		if distance < minimum:
			minimum = distance
			cnt[minimum] += 1
			tag = key
	return tag if cnt[minimum] == 1 else -1

for i in range(500):
	for j in range(500):
		matrix[i][j] = get_closest((i,j))
        
def get_outtermost_points(matrix):
    dimension = matrix.shape[0]
    arr = np.array((matrix[0,:],matrix[dimension-1,:],matrix[:,0],matrix[:,dimension-1]))
    return np.unique(arr)
    
outer_most_points = get_outtermost_points(matrix)
for outer in outer_most_points:
    matrix[matrix == outer] = -1
    
cnt = Counter(matrix.flatten())
#most common #1 will be -1
cnt.most_common(2)



