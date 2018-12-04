arr = []
found = False

def compare(w1, w2):
	length = len(w1)
	result = []
	for i in range(length):
		if(w1[i] == w2[i]):
			result.append(w1[i])

	return result

with open('day2input.txt') as f:
	for line in f:
		arr.append(line)

for w1 in arr:
	if(found): break
	for w2 in arr:
		result = compare(w1, w2)
		if(len(result) == len(w1)-1):
			print("".join(result))
			found = True
			break



