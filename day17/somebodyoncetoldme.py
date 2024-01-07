from math import inf
from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class A_star():
    cost: int
    cheapest_path: int = 999999
    best_guess: int = 999999
    consecutive_steps: int = 0
    direction_of_travel: str = ''
    def __lt__(self,a):
        return self.best_guess < a.best_guess
    
def heur(row,col,h,w):
    return((h-row) + (w-col))

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
    grid.append([ A_star(int(i)) for i in list(l.strip()) ])
height = len(grid)
width = len(grid[0])
grid[0][0].cheapest_path = 0
grid[0][0].best_guess = heur(0,0,height,width)

open_set = PriorityQueue()
open_set.put((grid[0][0].best_guess,0,0))

while open_set.not_empty:
    guess,row,col = open_set.get()
    if (row,col) == (height-1,width-1):
        print(guess)
        break
    cur = grid[row][col]
    if cur.best_guess < guess:
        pass  # continue  # already found a better path, pretty sure this should never happen
    neighbors = [(row+1, col),(row-1, col),(row, col+1),(row, col-1)]
    for n_row,n_col in neighbors:
        if n_row == -1 or n_col == -1 or n_row == height or n_col == width:
            continue  #  outside grid
        if cur.direction_of_travel == get_dir(row,col,n_row,n_col) and cur.consecutive_steps == 3:
            continue  #  already gone the maximum steps in this direction
        if get_reverse(cur.direction_of_travel) == get_dir(row,col,n_row,n_col):
            continue  # can't make a u-turn
        tentative = cur.cheapest_path + grid[n_row][n_col].cost
        if tentative < grid[n_row][n_col].cheapest_path:
            grid[n_row][n_col].cheapest_path = tentative
            grid[n_row][n_col].best_guess = tentative + heur(n_row,n_col,height,width)
            grid[n_row][n_col].direction_of_travel = get_dir(row,col,n_row,n_col)
            grid[n_row][n_col].src = (row,col)
            if cur.direction_of_travel == grid[n_row][n_col].direction_of_travel:
                grid[n_row][n_col].consecutive_steps = cur.consecutive_steps + 1
            else:
                grid[n_row][n_col].consecutive_steps = 1
            open_set_points = [ i[1:] for i in open_set.queue ]
            if open_set_points.count((n_row,n_col)) == 0:
                open_set.put((grid[n_row][n_col].best_guess,n_row,n_col))
    
src = (height-1,width-1)
path = [src]
while src != (0,0):
    row,col = src
    src = grid[row][col].src
    path.append(src)

path.reverse()
path = path[1:]
trtab = str.maketrans('UDLR','^v<>')
for i in range(len(grid)):
    tmp = ''
    for j in range(len(grid[i])):
        if (i,j) in path:
            tmp += grid[i][j].direction_of_travel
        else:
            tmp += str(grid[i][j].cost)
    print(tmp.translate(trtab))

