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

    def tilt(self):
        for i in range(1,len(self.grid)): # don't need to move rocks already in the top row
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'O':
                    self.roll(i, j, 'N')
    
with open('input') as f:
    lines = f.readlines()

    grid = Platform(lines)

    grid.tilt()

    weight = 0

    for i in range(len(grid.grid)):
        for j in grid.grid[i]:
            if j == 'O':
                weight += len(grid.grid) - i

    print(weight)