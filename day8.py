
# coding: utf-8

# In[16]:


content = ""

with open('day8input.txt') as f:
    for line in f:
        content += line.rstrip()
        
arr = content.split(' ')

meta_data = []
nodes = []
counter = 0

class Node:
    def __init__(self, child_count, md_count):
        self.child_count = child_count
        self.md_count = md_count
        self.metadatas = []
        self.children = []
            
    def add_child(self, child):
        self.children.append(child)
        
    def add_metadatas(self, metadatas):
        self.metadatas.extend(metadatas)
        
    def get_value(self):
        if(self.child_count == 0):
            return sum(int(md) for md in self.metadatas)
        else:
            value = 0
            for md in self.metadatas:
                md_int = int(md)
                if(md_int <= len(self.children)):
                    value += self.children[md_int-1].get_value()
            return value
        
    def print(self):
        print("child count: " + str(self.child_count))
        print("metadata count: " + str(self.md_count))
        print("metadata: " + str(self.metadatas))
        print("children: " + str(self.children))

def recursive_get_node(start):
    child_count = int(arr[start])
    md_count = int(arr[start+1])
    node = Node(child_count, md_count)
    
    child_start = start+2
    
    if(child_count > 0):
        for i in range(child_count):
            child_start, child_node = recursive_get_node(child_start)
            node.add_child(child_node)
            
    md_start = child_start
    
    if(md_count > 0):
        node.add_metadatas(arr[md_start : md_start + md_count])
        
    nodes.append(node)
    
    return md_start + md_count, node

recursive_get_node(0)

#part I

part1_ans = 0

for node in nodes:
    part1_ans += sum([int(md) for md in node.metadatas])
    
print(part1_ans)

#part II

print(nodes[len(nodes)-1].get_value())
    

