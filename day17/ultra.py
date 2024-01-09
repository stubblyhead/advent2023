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

with open('testcase') as f:
    lines = f.readlines()

grid = []
for l in lines:
    grid.append([ int(i) for i in list(l.strip()) ])
height = len(grid)
width = len(grid[0])