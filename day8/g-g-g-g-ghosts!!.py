from itertools import cycle

with open('testcase3') as f:
    lines = f.readlines()

# dirs = cycle(lines[0].strip())

# nodes = {}

# for i in lines[2:]: # first line is the directions, next line is just a``
#     (node, dests) = i.split(' = ')
#     (left, right) = [dests[1:4], dests[6:9]]
#     nodes[node] = [left,right]

# stepcount = 0

# cur_node = 'AAA'

# for n in dirs:
#     stepcount += 1  # increment the number of steps
#     if n == 'L':
#         cur_node = nodes[cur_node][0]  # next node is the left one
#     else:
#         cur_node = nodes[cur_node][1]  # next node is the right one
#     if cur_node == 'ZZZ':
#         break  # we're at the destination, so break out of the loop

# print(stepcount)

