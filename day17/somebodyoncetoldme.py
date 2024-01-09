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


open_set = [(0,0,0,'R',0)]
seen = set()

# while open_set:
#     cheapest_path,row,col,prev_dir,steps = heappop(open_set)
#     if (row,col,prev_dir,steps) in seen:
#         continue
#     seen.add((row,col,prev_dir,steps))

#     if (row,col) == (height-1,width-1):
#         print(cheapest_path)
#         break
#     neighbors = [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
#     for n_row,n_col in neighbors:
#         if n_row == -1 or n_col == -1 or n_row == height or n_col == width:
#             continue  #  outside grid
#         direction = get_dir(row,col,n_row,n_col)
#         if get_reverse(prev_dir) == direction:
#             continue
#         if steps < 3 and direction == prev_dir:
#             heappush(open_set, (cheapest_path + grid[n_row][n_col], n_row, n_col, direction, steps+1))
#         elif direction != prev_dir:
#             heappush(open_set, (cheapest_path + grid[n_row][n_col], n_row, n_col, direction, 1))
#         else:
#             continue
def calc_cheapest(prev_cheap, row, col, prev_dir, new_dir, grid):
    height = len(grid)
    width = len(grid[0])
    if prev_dir == new_dir:
        if row == -1 or col == -1 or row == height or col == width:
            return -1
        elif steps < 10:
            return prev_cheap + grid[row][col]
        else:
            return -1
    if new_dir == 'U' and row < 3 or new_dir == 'D' and row > height - 4 or new_dir == 'L' and col < 3 or new_dir == 'R' and col > width - 4:
        return -1
    else:
        if new_dir == 'U':
            for i in range(row,row-4,-1):
                prev_cheap += grid[i][col]
        elif new_dir == 'D':
            for i in range(row,row+4):
                prev_cheap += grid[i][col]
        elif new_dir == 'R':
            for i in range(col,col+4):
                prev_cheap += grid[row][i]
        elif new_dir == 'L':
            for i in range(n_col,n_col-4,-1):
                prev_cheap += grid[n_row][i]
        return prev_cheap




open_set = [(0,0,0,'R',10),(0,0,0,'D',10)]
seen = set()
while open_set:
    cheapest_path,row,col,prev_dir,steps = heappop(open_set)
    if (row,col,prev_dir,steps) in seen:
        continue
    if row == -1 or col == -1 or row == height or col == width:
        continue
    seen.add((row,col,prev_dir,steps))
    if (row,col) == (height-1,width-1):
        print(cheapest_path)
        break
    neighbors = [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
    for n_row,n_col in neighbors:
        new_dir = get_dir(row,col,n_row,n_col)
        if new_dir == get_reverse(prev_dir):
            continue
        new_cheap = calc_cheapest(cheapest_path,n_row,n_col,prev_dir,new_dir,grid)
        if new_cheap == -1:
            continue
        else:
            if new_dir == prev_dir: 
                heappush(open_set,(new_cheap,n_row,n_col,new_dir,steps+1))
            else:
                if new_dir == 'D':
                    heappush(open_set,(new_cheap,n_row+3,n_col,new_dir,4))
                elif new_dir == 'U':
                    heappush(open_set,(new_cheap,n_row-3,n_col,new_dir,4))
                elif new_dir == 'R':
                    heappush(open_set,(new_cheap,n_row,n_col+3,new_dir,4))
                elif new_dir == 'L':
                    heappush(open_set,(new_cheap,n_row,n_col-3,new_dir,4))
                

