class Pipes:
    def __init__(self, layout):
        # not sure if I'll need these but why not
        self.width = len(layout[0])
        self.height = len(layout)
        self.layout = layout

        for i in range(len(layout)):
            if layout[i].find('S') >= 0:  # start is in this row
                self.start_row = i
                self.start_col = layout[i].index('S')
                break

    def get_next(cur, origin):
        dests = { '|': ['S','N'],
                  '-': ['E','W'],
                  'L': ['N','E'],
                  'J': ['N','W'],
                  '7': ['W','S'],
                  'F': ['E','S']
                 }
        cxn = dests[cur] # get directions this tile can go
        cxn.remove(origin) # get rid of the one we came from
        return cxn[0] # the one that's left is the directon we go next
    
    def get_opposite(dir):
        if dir == 'N':
            return 'S'
        if dir == 'S':
            return 'N'
        if dir == 'E':
            return 'W'
        if dir == 'W':
            return 'E'


    def traverse(self):
        self.path = []
        self.path.append([self.start_row, self.start_col])
        origin = ''
        # find an exit from starting point
        if self.start_row > 0: # look north unless we're in the top row
            north = self.layout[self.start_row-1][self.start_col]
            if north in ['|', 'F', '7']:
                self.path.append([self.start_row - 1, self.start_col])
                origin = 'S'
        if self.start_row < self.height - 1 and not origin: # look south unless we're on the last row and we haven't already found an exit
            south = self.layout[self.start_row +1][self.start_col]
            if south in ['|', 'J', 'L' ]:
                self.path.append([self.start_row + 1, self.start_col])
                origin = 'N'
        if self.start_col > 0 and not origin: # look west unless we're on the left edge and havne't found an exit
            west = self.layout[self.start_row][self.start_col - 1]
            if west in ['L', '-', 'F']:
                self.path.append([self.start_row, self.start_col - 1])
                origin = 'E'
        if self.start_col < self.width - 1 and not origin: # look east unless we're on the right edge and haven't found an exit
            east = self.layout[self.start_row][self.start_col + 1]
            if east in ['-', 'J', '7']:
                self.path.append([self.start_row, self.start_col + 1])
                origin = 'W'
        while self.path[-1] != [self.start_row, self.start_col]:  # when we get back to the beginning we've got a full loop
            (cur_row, cur_col) = self.path[-1]  # get the row and col of the last tile
            next_dir = Pipes.get_next(self.layout[cur_row][cur_col], origin)
            if next_dir == 'N':
                self.path.append([cur_row - 1, cur_col])
            elif next_dir == 'S':
                self.path.append([cur_row + 1, cur_col])
            elif next_dir == 'E':
                self.path.append([cur_row, cur_col + 1])
            elif next_dir == 'W':
                self.path.append([cur_row, cur_col - 1])
            origin = Pipes.get_opposite(next_dir)
            


with open('testcase') as f:
    lines = [ i.strip() for i in f.readlines() ]

my_maze = Pipes(lines)

my_maze.traverse()

print(len(my_maze.path) // 2) # farthest away is half of the total length
            