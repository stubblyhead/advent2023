from math import inf
from dataclasses import dataclass
@dataclass
class Leg():
    remaining: int = 3
    arrived_heading: str = ''

@dataclass
class Tile:
    cost: int
    leg: Leg


class Grid:
    def __init__(self, layout):

        self.layout = []
        for i in layout:
            self.layout.append( [ Tile(int(j),Leg()) for j in list(i.strip())] )
        self.height = len(self.layout)
        self.width = len(self.layout[0])

    def search(self):
        start = [0,0]
        end = [self.height-1,self.width-1]
        open_set = [start]

        cheapest_to_here = []
        best_guess = []
        best_path_to_here = []
        for i in self.layout:
            l = [ inf for j in i ]
            cheapest_to_here.append(list(l))
            best_guess.append(list(l))
            best_path_to_here.append([ [] for j in i ])
        cheapest_to_here[0][0] = 0
        best_guess[0][0] = self.heur(0,0)
        best_path_to_here[0][0] = [[0,0]]

        while open_set:
            # find space on frontier with lowest known score
            current = []
            min_score = inf
            for (row,col) in open_set:
                if best_guess[row][col] < min_score:
                    min_score = best_guess[row][col]
                    current = [row,col]
            if current == end:
                print(best_path_to_here[current[0]][current[1]])
                return cheapest_to_here[current[0]][current[1]]
            open_set.remove(current)
            cur_row, cur_col = current
            neighbors = self.get_neighbors(cur_row, cur_col)
            for dir in neighbors:
                # if len(best_path_to_here[cur_row][cur_col]) > 3:
                #       three_ago_row,three_ago_col = best_path_to_here[cur_row][cur_col][-4]
                #       if (three_ago_row == n_row and abs(three_ago_col - n_col) > 3) \
                #       or (three_ago_col == n_col and abs(three_ago_row - n_row) > 3):
                #           continue # already went 3 in this direction, so we can't go this way
                n_row, n_col = cur_row, cur_col
                if dir == 'N':
                    n_row -= 1
                elif dir == 'S':
                    n_row += 1
                elif dir == 'E':
                    n_col += 1
                elif dir == 'W':
                    n_col -= 1

                tentative_score = cheapest_to_here[cur_row][cur_col] + self.layout[n_row][n_col].cost
                if tentative_score < cheapest_to_here[n_row][n_col]:
                    cheapest_to_here[n_row][n_col] = tentative_score
                    self.layout[n_row][n_col].leg.arrived_heading = dir
                    if self.layout[cur_row][cur_col].leg.arrived_heading == dir:
                        self.layout[n_row][n_col].leg.remaining = self.layout[cur_row][cur_col].leg.remaining - 1
                    else:
                        self.layout[n_row][n_col].leg.remaining = 2
                    best_guess[n_row][n_col] = tentative_score + self.heur(n_row, n_col)
                    best_path_to_here[n_row][n_col] = best_path_to_here[cur_row][cur_col] + [[n_row,n_col]]
                    if [n_row, n_col] not in open_set:
                        open_set.append([n_row,n_col])

            
    
    def heur(self,row,col):
        # using manhattan distance for lower bound
        return ((self.height - row) + (self.width - col))
    
    def get_neighbors(self,row,col):
        neighbors = []
        if row != 0 and self.layout[row][col].leg.arrived_heading != 'S': # not at the top and didn't get here by going south (i.e. not a u-turn)
            if not (self.layout[row][col].leg.arrived_heading == 'N' and self.layout[row][col].leg.remaining == 0): # haven't just made 3 N moves in a row
                neighbors.append('N')
        if col != 0 and self.layout[row][col].leg.arrived_heading != 'E':
            if not (self.layout[row][col].leg.arrived_heading == 'W' and self.layout[row][col].leg.remaining == 0):
                neighbors.append('W')
        if row != self.height - 1 and self.layout[row][col].leg.arrived_heading != 'N':
            if not (self.layout[row][col].leg.arrived_heading == 'S' and self.layout[row][col].leg.remaining == 0):
                neighbors.append('S')   
        if col != self.width -1 and self.layout[row][col].leg.arrived_heading != 'W':
            if not (self.layout[row][col].leg.arrived_heading == 'E' and self.layout[row][col].leg.remaining == 0):
                neighbors.append('E')

        return neighbors

with open('testcase') as f:
    lines = f.readlines()

my_grid = Grid(lines)

print(my_grid.search())