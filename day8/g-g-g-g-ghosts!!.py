from itertools import cycle

with open('testcase3') as f:
    lines = f.readlines()

dirs = cycle(lines[0].strip())

nodes = {}

for i in lines[2:]: # first line is the directions, next line is just a``
        (node, dests) = i.split(' = ')
        (left, right) = [dests[1:4], dests[6:9]]
        nodes[node] = [left,right]

def get_steps(nodes, dirs, start_node):
    stepcount = 0
    cur_node = start_node
    for n in dirs:
        stepcount += 1  # increment the number of steps
        if n == 'L':
            cur_node = nodes[cur_node][0]  # next node is the left one
        else:
            cur_node = nodes[cur_node][1]  # next node is the right one
        if cur_node[-1] == 'Z':
            break  # we're at the destination, so break out of the loop

    return(stepcount)

stepcount = 1
for n in nodes.keys():
    if n[-1] == 'A':
        thiscount = get_steps(nodes, dirs, n)
        if n == 'AAA':
            print(thiscount)
        stepcount *= thiscount
print(stepcount)

# stepcount = 0

# cur_nodes = []
# for n in nodes.keys():
#     if n[-1] == 'A':
#         cur_nodes.append(n)  # add nodes to cur_nodes list if last letter is A

# for d in dirs:
#     z_count = 0 # keep track of Z-node count in each loop so we don't need to loop through a second time
#     stepcount += 1  # increment the number of steps
#     for i in range(len(cur_nodes)):
#         if d == 'L':
#             cur_nodes[i] = nodes[cur_nodes[i]][0]  # next node is the left one            
#         else:
#             cur_nodes[i] = nodes[cur_nodes[i]][1]  # next node is the right one
        
#         if cur_nodes[i][-1] == 'Z':
#             z_count += 1
    
#     if z_count == len(cur_nodes):
#         break  # we're at the destination, so break out of the loop

# print(stepcount)