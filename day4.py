import numpy as np

def getInfoType(string):
	if(string.startswith("Guard", 1)):
		return 'guard'
	elif(string.startswith("falls", 1)):
		return 'sleep'
	elif(string.startswith("wakes",1)):
		return 'wake'

def getGuardNum(string):
	arr = string.split(' ')
	return int(arr[2][1:])

def getTime(string):
	length = len(string)
	return int(string[length-2] + string[length-1])

def getMaxTotal(totals):
	maximum = 0
	for key in totals:
		if totals[key] > maximum:
			maximum = totals[key]
			guard = key
	return guard

def getMaxOverlap(ranges):
	mins = np.zeros(60)
	for (start,end) in ranges:
		mins[start:end] += 1
	return np.argmax(mins)

def getMaxOverlapCount(ranges):
	mins = np.zeros(60)
	for (start,end) in ranges:
		mins[start:end] += 1
	return mins.max()	

def getMostFrequentlyAsleepOnSameMin(ranges):
	maximum = 0
	for key in ranges:
		maxOverlapCount = getMaxOverlapCount(ranges[key])
		if maxOverlapCount > maximum:
			maximum = maxOverlapCount
			guard = key
	return guard


schedules = []
total_guards_asleep = {}
guards_asleep_intervals = {}

with open('day4input.txt') as f:
	for line in f:
		schedules.append(line[:len(line)-1])

	schedules.sort()

	for s in schedules:
		splited = s.split(']')
		time = splited[0]
		info = splited[1]
		if(getInfoType(info) == 'guard'):
			currentGuard = getGuardNum(info)
			if(currentGuard not in guards_asleep_intervals):
				guards_asleep_intervals[currentGuard] = []
			if(currentGuard not in total_guards_asleep):
				total_guards_asleep[currentGuard] = 0
		elif(getInfoType(info) == 'sleep'):
			asleepMin = getTime(time)
		elif(getInfoType(info) == 'wake'):
			awakeMin = getTime(time)
			total_guards_asleep[currentGuard] += (awakeMin - asleepMin)
			guards_asleep_intervals[currentGuard].append((asleepMin, awakeMin))

	#part 1
	guardNum = getMaxTotal(total_guards_asleep)
	print(guardNum)
	max_overlap_min = getMaxOverlap(guards_asleep_intervals[guardNum])
	print(max_overlap_min)

	#part 2
	guardNum2 = getMostFrequentlyAsleepOnSameMin(guards_asleep_intervals)
	print(guardNum2)
	max_overlap_min = getMaxOverlap(guards_asleep_intervals[guardNum2])
	print(max_overlap_min)


