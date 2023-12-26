from math import inf

class Grid:
    def __init__(self, layout):

        self.layout = []
        for i in layout:
            self.layout.append( [ int(j) for j in list(i.strip())] )
        self.height = len(self.layout)
        self.width = len(self.layout[0])

    def search(self):
        start = [0,0]
        end = [self.height-1,self.width-1]
        open_set = [start]

        cheapest_to_here = []
        best_guess = []
        for i in self.layout:
            l = [ inf for j in i ]
            cheapest_to_here.append(list(l))
            best_guess.append(list(l))
        cheapest_to_here[0][0] = 0
        best_guess[0][0] = self.heur(0,0)

        while open_set:
            # find space on frontier with lowest known score
            current = []
            min_score = inf
            for (row,col) in open_set:
                if best_guess[row][col] < min_score:
                    min_score = best_guess[row][col]
                    current = [row,col]
            if current == end:
                return min_score
            open_set.remove(current)
            cur_row, cur_col = current
            neighbors = self.get_neighbors(cur_row, cur_col)
            for (n_row, n_col) in neighbors:
                tentative_score = cheapest_to_here[cur_row][cur_col] + self.layout[n_row][n_col]
                if tentative_score < cheapest_to_here[n_row][n_col]:
                    cheapest_to_here[n_row][n_col] = tentative_score
                    best_guess[n_row][n_col] = tentative_score + self.heur(n_row, n_col)
                    if [n_row, n_col] not in open_set:
                        open_set.append([n_row,n_col])

            
    
    def heur(self,row,col):
        # using manhattan distance for lower bound
        return ((self.height - row) + (self.width - col))
    
    def get_neighbors(self,row,col):
        neighbors = [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]
        to_remove = []
        for tile in neighbors:
            if -1 in tile or tile[0] == self.height or tile[1] == self.width:
                to_remove.append(tile)
        for tile in to_remove:
            neighbors.remove(tile)
        return neighbors

with open('testcase') as f:
    lines = f.readlines()

my_grid = Grid(lines)

print(my_grid.search())