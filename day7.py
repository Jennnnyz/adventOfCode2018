import re
from collections import Counter

instr = []
#key:child, value:list of its parents
c2p = {}
#key:parent, value:list of children
p2c = {}

with open('day7input.txt') as f:
    for line in f:
        line = line.rstrip()
        match = re.match(r'Step (.*) must be finished before step (.*) can begin.', line)
        instr.append((match.group(1), match.group(2)))

#parent must be completed before children can begin
for pair in instr:
    if(pair[0] not in p2c):
        p2c[pair[0]] = [pair[1]]
    else:
        p2c[pair[0]].append(pair[1])
        p2c[pair[0]].sort()
        
for pair in instr:
    if(pair[1] not in c2p):
        c2p[pair[1]] = [pair[0]]
    else:
        c2p[pair[1]].append(pair[0])
        c2p[pair[1]].sort()

visited = []

def reverse_sort(arr):
    return sorted(arr, reverse=True)

#get starting alphabets = alphabets with no parents
to_visit = [p for p in p2c if p not in c2p and p not in visited]
to_visit = reverse_sort(to_visit)

#an alphabet can be visited if it's not been visited or all of its parents have been visited
def can_visit(arr):
    return [a for a in arr if a not in visited and len(c2p[a]) == 0]

#------------part II-----------------

cnt = Counter()
worker_available = 5

def visit(alphabets):
    for alphabet in alphabets:
        if(cnt[alphabet] == (ord(alphabet)-5)):
            visited.append(alphabet)
            for c in c2p:
                if alphabet in c2p[c]:
                    c2p[c].remove(alphabet)
        cnt[alphabet] += 1
    
time_elapsed = 0

while len(to_visit) > 0:
    needed_workers = len(to_visit) if len(to_visit) < worker_available else worker_available
    alphabets = to_visit[:needed_workers]
    visit(alphabets)
    for alphabet in alphabets:
        if alphabet in visited:
            to_visit.remove(alphabet)
            #now that we've visited the parent, we can visit the children
            if alphabet in p2c:
                children = p2c[alphabet]
                visitable = reverse_sort(can_visit(children))
                to_visit.extend(visitable)
    time_elapsed += 1
    
print(time_elapsed)

#------------part I-----------------

def visit(alphabet):
    visited.append(alphabet)
    for c in c2p:
        if alphabet in c2p[c]:
            c2p[c].remove(alphabet)

while len(to_visit) > 0:
    to_visit = reverse_sort(to_visit)
    alphabet = to_visit.pop()
    print("visiting "+alphabet)
    visit(alphabet)
    if alphabet in p2c:
        children = p2c[alphabet]
        visitable = reverse_sort(can_visit(children))
        to_visit.extend(visitable)

print(''.join(visited))

