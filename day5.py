from string import ascii_lowercase

def remove(alphabet, content):
	content = content.replace(alphabet, '')
	content = content.replace(alphabet.upper(), '')
	return content

#part I
def react(content):

	previous_len = 0

	while(previous_len != len(content)):
		counter = 0
		previous_len = len(content)
		content_arr = list(content)
		while(counter < len(content_arr)-1):
			current = content_arr[counter]
			nxt = content_arr[counter+1]
			if(current.upper() == nxt.upper()):
				if(current.upper() == nxt and nxt.lower() == current) or (current.lower() == nxt and nxt.upper() == current):
					content_arr[counter] = '0'
					content_arr[counter+1] = '0'
					counter += 1

			counter += 1
		content = ''.join(content_arr)
		content = content.replace('0', '')

	return content

with open('day5input.txt') as f:
	content = f.read().rstrip()

#50000 = length of total characters
minimum = 50000
for alphabet in ascii_lowercase:
	content_copy = content
	stripped = remove(alphabet, content_copy)
	reacted = react(stripped)
	length = len(reacted)
	if(length < minimum):
		minimum = length

#part II
print(minimum)