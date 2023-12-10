from itertools import cycle
from math import gcd

with open('input') as f:
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

counts = []
for n in nodes.keys():
    if n[-1] == 'A':
        thiscount = get_steps(nodes, dirs, n)
        if n == 'AAA':
            print(thiscount)
        counts.append(thiscount)
# need least common multiple of individual counts

stepcount = 1
for i in counts:
    # for each starting node's count, multiply by the current total count and
    # divide by the greatest common denominator
    factor = gcd(stepcount,i)
    stepcount = stepcount * i // factor
    
print(stepcount)