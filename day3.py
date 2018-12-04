import numpy as np

matrix = np.zeros((1000,1000))
isOverlapped = {}


def getID(line):
	arr = line.split('@')
	ID = int(arr[0][1:])
	return ID

def getLeftTopEdge(line):
	arr = line.split('@')
	edges = arr[1].split(':')[0]
	left = int(edges.split(',')[0])
	top = int(edges.split(',')[1])
	return (left, top)


def getDimension(line):
	arr = line.split(':')
	dimension = arr[1].split('x')
	width = int(dimension[0])
	height = int(dimension[1])
	return (width, height)

with open('day3input.txt') as f:
	for line in f:
		count = 0
		ID = getID(line)
		isOverlapped[ID] = False
		(left, top) = getLeftTopEdge(line)
		(width, height) = getDimension(line)
		for i in range(height) :
			for j in range(width):
				if(matrix[top+i][left+j] != 0):
					isOverlapped[matrix[top+i][left+j]] = True
					isOverlapped[ID] = True
				
				matrix[top+i][left+j] = ID

	for key in isOverlapped:
		if(not isOverlapped[key]):
			print(key)
