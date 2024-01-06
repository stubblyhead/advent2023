with open('testcase') as f:
    lines = f.readlines()

grid = [ list(l.strip()) for l in lines ]
height = len(grid)
width = len(grid[0])
energized = [ [ '.' for i in range(width)] for j in range(height) ]
energized[0][0] = '#'
beams = []
beams.append([(0,0,'R')])
visited = [(0,0,'R')]  # if a beam enters a tile traveling the same direction as a previous beam then we can ignore it

def reflect(m, d):
    if d == 'R' and m == '\\' or d == 'L' and m == '/':
        return 'D'
    elif d == 'R' and m == '/' or d == 'L' and m == '\\':
        return 'U'
    elif d == 'U' and m == '\\' or d == 'D' and m == '/':
        return 'L'
    else:
        return 'R'

while beams:  #  will add beams as they're created, and remove them as they exit the grid or start to loop
    prune = []
    add = []
    for i in range(len(beams)):
        row,col,dir = beams[i][-1]
        if dir == 'R':
            col += 1
        elif dir == 'L':
            col -= 1
        elif dir == 'U':
            row -= 1
        elif dir == 'D':
            row += 1
        if col == -1 or row -1 or col == width or row == height:
            prune.append(i)  #  beam has exited the grid
            continue
        if grid[row][col] == '\\' or grid[row][col] == '/':
            dir = reflect(grid[row][col], dir)
        if grid[row][col] == '-' and (dir == 'U' or dir == 'D'):
            dir = 'L'
            add.append(row,col,'R')
        if grid[row][col] == '|' and (dir == 'L' or dir == 'R'):
            dir == 'U'
            add.append(row,col,'D')
        if visited.index((row,col,dir)) >= 0:
            prune.append(i)  # don't need to keep tracking this beam
            continue

        energized[row][col] = '#'  # mark this square as being energized
        prune.sort(reverse=True)
        for i in prune:
            beams.pop(i)
        beams += add

count = 0
for i in energized:
    count += i.count('#')

print(count)
            