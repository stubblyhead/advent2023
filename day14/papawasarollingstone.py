class Platform:
    def __init__(self, layout):
        self.grid = [ list(i.strip()) for i in layout ] # 2-D list, each char in its own slot

    def roll(self, row, col):
        grid_col = [ i[col] for i in self.grid ] # get array of this col
        while True:
            if grid_col[row - 1] == '.':
                grid_col[row - 1] == 'O' # move rock up a space
                grid_col[row] == '.' # rock isn't here anymore, so make it a .
                row -= 1 # go up a row
            else:
                break
            if row == 0:  # stop if the rock is in the top row
                break

    def tilt(self):
        for i in range(1,len(self.grid)): # don't need to move rocks already in the top row
            for j in range(len(i)):
                if self.grid[i][j] == 'O':
                    self.roll(self, i, j)
    

    



with open('testcase') as f:
    lines = f.readlines()

