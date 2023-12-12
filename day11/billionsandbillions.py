import numpy as np

def taxi_dist(a,b):
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dist


with open('input') as f:
    lines = f.readlines()

map = [ [ i for i in list(j.strip()) ] for j in lines ]
width = len(map)
height = len(map[0])

tempmap = []
for i in map:
    if i.count('#') == 0:
        tempmap += [i,i]  # add current line twice if there are no galaxies
    else: 
        tempmap += [i]  # otherwise only add once

map = list(tempmap)
txpose = np.array(map)
txpose = txpose.transpose()
map = txpose.tolist()

#  now do this again after transposing
tempmap = []
for i in map:  
    if i.count('#') == 0:
        tempmap += [i,i]
    else:
        tempmap += [i]
map = list(tempmap)

galaxies = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            galaxies.append([i,j])

totaldist = 0
for i in range(len(galaxies)-1):
    for j in range(i,len(galaxies)):
        totaldist += taxi_dist(galaxies[i],galaxies[j])

print(totaldist)