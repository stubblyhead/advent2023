import numpy as np

def taxi_dist(a,b):
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dist


with open('testcase') as f:
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
txpose = np.array(map)
txpose = txpose.transpose()
map = txpose.tolist()
galaxies = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            galaxies.append([i,j])

totaldist = 0
for i in range(len(galaxies)-1):
    for j in range(i + 1,len(galaxies)):
        dist = taxi_dist(galaxies[i],galaxies[j])
        totaldist += dist
        print(dist)
print(totaldist)

# part two, going to try a different approach

map = [ [ i for i in list(j.strip()) ] for j in lines ]
empty_cols = []
empty_rows = []

for i in range(height):
    if map[i].count('#') == 0:
        empty_rows.append(i)
    
for i in range(width):
    for j in [[ x[i] for x in map ]]:
    
        if j.count('#') == 0:
            empty_cols.append(i)

galaxies = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            galaxies.append([i,j])

totaldist = 0
distcount = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1,len(galaxies)):
        dist = 0
        dist += taxi_dist(galaxies[i],galaxies[j])
        for r in empty_rows:
            top = min(galaxies[i][0],galaxies[j][0])
            bottom = max(galaxies[i][0],galaxies[j][0])
            if r > top and r < bottom:
                dist += 9 # already have one, need 1e6 total, so add 999999
        for r in empty_cols:
            left = min(galaxies[i][1],galaxies[j][1])
            right = max(galaxies[i][1],galaxies[j][1])
            if r > galaxies[i][1] and r < galaxies[j][1]:
                dist += 9 # already have one, need 1e6 total, so add 999999
        totaldist += dist
        print(dist)

print(totaldist)



