from heapq import heappop, heappush


def get_dir(row,col,n_row,n_col):
    if row == n_row:
        if n_col > col:
            return 'R'
        else:
            return 'L'
    elif col == n_col:
        if n_row > row:
            return 'D'
        else:
            return 'U'

def get_reverse(dir):
    if dir == 'U':
        return 'D'
    elif dir == 'D':
        return 'U'
    elif dir == 'R':
        return 'L'
    elif dir == 'L':
        return 'R'

with open('input') as f:
    lines = f.readlines()

grid = []
for l in lines:
    grid.append([ int(i) for i in list(l.strip()) ])
height = len(grid)
width = len(grid[0])


open_set = [(0,0,0,'R',0)]
seen = set()
seen_count = 0
while open_set:
    cheapest_path,row,col,prev_dir,steps = heappop(open_set)
    if (row,col,prev_dir,steps) in seen:
        continue
    seen.add((row,col,prev_dir,steps))

    if (row,col) == (height-1,width-1):
        print(cheapest_path)
        break
    neighbors = [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
    for n_row,n_col in neighbors:
        if n_row == -1 or n_col == -1 or n_row == height or n_col == width:
            continue  #  outside grid
        direction = get_dir(row,col,n_row,n_col)
        if get_reverse(prev_dir) == direction:
            continue
        if steps < 3 and direction == prev_dir:
            heappush(open_set, (cheapest_path + grid[n_row][n_col], n_row, n_col, direction, steps+1))
        elif direction != prev_dir:
            heappush(open_set, (cheapest_path + grid[n_row][n_col], n_row, n_col, direction, 1))
        else:
            continue
        
