with open('input') as f:
    lines = f.readlines()

dir = []
dist = []
color = []

for l in lines:
    i,j,k = l.strip().split()
    dir.append(i)
    dist.append(int(j))
    color.append(k[1:-1]) # assuming the parens don't matter

# need to figure out where the starting point even is
max_left = 0
max_right = 0
max_up = 0
max_down = 0
x = 0
y = 0
for i in range(len(dir)):
    if dir[i] == 'L':
        x -= dist[i]
        max_left = min(max_left,x)
    elif dir[i] == 'R':
        x += dist[i]
        max_right = max(max_right,x)
    elif dir[i] == 'U':
        y -= dist[i]
        max_up = min(max_up, y)
    else:
        y += dist[i]
        max_down = max(max_down,y)


grid = [ [ '.' for j in range(max_right + abs(max_left) + 1) ] for i in range(max_down + abs(max_up) + 1) ] 

p_row, p_col = abs(max_up), abs(max_left)
grid[p_row][p_col] = '#'

for i in range(len(dir)):
    if dir[i] == 'U':
        for j in range(dist[i]):
            p_row -= 1
            grid[p_row][p_col] = '#'

    elif dir[i] == 'D':
        for j in range(dist[i]):
            p_row += 1
            grid[p_row][p_col] = '#'

    elif dir[i] == 'L':
        for j in range(dist[i]):
            p_col -= 1
            grid[p_row][p_col] = '#'

    elif dir[i] == 'R':
        for j in range(dist[i]):
            p_col += 1
            grid[p_row][p_col] = '#'

# for i in grid:
#     templine = ''
#     for j in i:
#         templine += j
#     print(templine)
            
# flood fill, start on second row down since top row cannot have any interior spaces

# find interior space
first_border = grid[1].index('#')
first_interior = grid[1][first_border:].index('.') + first_border

fill_queue = [[1,first_interior]]

while fill_queue:
    row,col = fill_queue.pop(0)
    if grid[row][col] == '#':
        continue
    grid[row][col] = '#'
    fill_queue += [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]

dig_count = 0
for i in grid:
    for j in i:
        if j == '#':
            dig_count += 1 

print(dig_count)
