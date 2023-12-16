class Platform:
    def __init__(self, layout):
        self.grid = [ list(i.strip()) for i in layout ] # 2-D list, each char in its own slot

    def roll(self, row, col, dir):
        if dir == 'N' or dir == 'S':
            grid_col = [ i[col] for i in self.grid ] # get array of this col
            if dir == 'N':
                delta = -1
            else:
                delta = 1
            while True:
                if grid_col[row + delta] == '.':
                    self.grid[row + delta][col] = 'O' # move rock one space
                    self.grid[row][col] = '.' # rock isn't here anymore, so make it a .
                    row = row + delta # move one row over
                else:
                    break
                if row == 0 or row == len(self.grid) - 1:  # stop if the rock is in the top or bottom row
                    break
        if dir == 'E' or dir == 'W':
            grid_row = self.grid[row]
            if dir == 'E':
                delta = +1
            else:
                delta = -1
            while True:
                if grid_row[col + delta] == '.':
                    self.grid[row][col + delta] = 'O'
                    self.grid[row][col] = '.'
                    col = col + delta
                else:
                    break
                if col == 0 or col == len(self.grid[row]) -1:
                    break

    def tilt(self, dir):
        if dir == 'N':
            for i in range(1,len(self.grid)): # don't need to move rocks already in the top row
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] == 'O':
                        self.roll(i, j, dir)
        elif dir == 'S':
            for i in range(len(self.grid)-2,-1,-1):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] == 'O':
                        self.roll(i,j,dir)
        elif dir == 'W':
            for i in range(len(self.grid)):
                for j in range(1,len(self.grid[i])):
                    if self.grid[i][j] == 'O':
                        self.roll(i,j,dir)
        elif dir == 'E':
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])-2,-1,-1):
                    if self.grid[i][j] == 'O':
                        self.roll(i,j,dir)

    def spin(self):
        self.tilt('N')
        self.tilt('W')
        self.tilt('S')
        self.tilt('E')
    
with open('testcase') as f:
    lines = f.readlines()

    grid = Platform(lines)

    for i in range(3):
        grid.spin()
    # weight = 0

    # for i in range(len(grid.grid)):
    #     for j in grid.grid[i]:
    #         if j == 'O':
    #             weight += len(grid.grid) - i

    # print(weight)

    for i in grid.grid:
        print(str(i))