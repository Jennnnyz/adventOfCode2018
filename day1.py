sum = 0
counts = {}
found = False

while not found:
	with open('day1input.txt') as f:
		for line in f:
			if(sum in counts):
				print(sum)
				found = True
				break
			else:
				counts[sum] = 1
			if(line[0] == '+'):
				sum += int(line[1:])
			else:
				sum -= int(line[1:])



