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
        self.path.append((self.start_row, self.start_col))
        origin = ''
        # find an exit from starting point
        if self.start_row > 0: # look north unless we're in the top row
            north = self.layout[self.start_row-1][self.start_col]
            if north in ['|', 'F', '7']:
                self.path.append((self.start_row - 1, self.start_col))
                origin = 'S'
        if self.start_row < self.height - 1 and not origin: # look south unless we're on the last row and we haven't already found an exit
            south = self.layout[self.start_row +1][self.start_col]
            if south in ['|', 'J', 'L' ]:
                self.path.append((self.start_row + 1, self.start_col))
                origin = 'N'
        if self.start_col > 0 and not origin: # look west unless we're on the left edge and havne't found an exit
            west = self.layout[self.start_row][self.start_col - 1]
            if west in ['L', '-', 'F']:
                self.path.append([self.start_row, self.start_col - 1])
                origin = 'E'
        if self.start_col < self.width - 1 and not origin: # look east unless we're on the right edge and haven't found an exit
            east = self.layout[self.start_row][self.start_col + 1]
            if east in ['-', 'J', '7']:
                self.path.append((self.start_row, self.start_col + 1))
                origin = 'W'
        while self.path[-1] != (self.start_row, self.start_col):  # when we get back to the beginning we've got a full loop
            (cur_row, cur_col) = self.path[-1]  # get the row and col of the last tile
            next_dir = Pipes.get_next(self.layout[cur_row][cur_col], origin)
            if next_dir == 'N':
                self.path.append((cur_row - 1, cur_col))
            elif next_dir == 'S':
                self.path.append((cur_row + 1, cur_col))
            elif next_dir == 'E':
                self.path.append((cur_row, cur_col + 1))
            elif next_dir == 'W':
                self.path.append((cur_row, cur_col - 1))
            origin = Pipes.get_opposite(next_dir)
            
    def print_maze(self):  # may be useful in conceptualizing part two
        for i in range(self.height):
            templine = ''
            for j in range(self.width):
                c = self.layout[i][j]
                c = c.replace('7', "\u2510")  # replace alphanum w/ box drawing chars
                c = c.replace('J', "\u2518")
                c = c.replace('F', "\u250C")
                c = c.replace('L', "\u2514")
                c = c.replace('|', "\u2502")
                c = c.replace('-', "\u2500")
                if (i,j) in self.path:
                    c = "\033[91m" + c + "\033[0m"
                elif (i,j) in self.inside:
                    c = "\033[94m" + c + "\033[0m"
                elif (i,j) in self.outside:
                    c = "\033[92m" + c + "\033[0m"
                templine += c
            print(templine)

    def get_area(self):
        # start at upper left, assume outside the loop.  add tiles to outside set until
        # we hit the path.  next non-path will be inside.  if current tile and previous
        # tile are both vertical path members (i.e. not -) then inside/outside region was
        # zero width, so toggle what the next non-path will be

        path = self.path
        layout = self.layout
        (start_row,start_col) = path[0]
        inside = []
        outside = []
        start_tile = self.get_start_tile()
        self.layout[start_row] = self.layout[start_row][:start_col] + start_tile + self.layout[start_row][start_col+1:]
        

        for row in range(self.height):
            next_nonpath = 'O'
            for col in range(self.width):
                p = (row,col)
                
                if p not in path:  # junk tiles

                    if next_nonpath == 'O':
                        outside.append(p)
                    else:
                        inside.append(p)
                else:  # path tiles
                    cur = layout[row][col]

                    if col > 0:
                        
                        prev = layout[row][col-1]
                        prev_tile = (row,col-1)
                        cur_and_prev = prev + cur
                    else:
                        next_nonpath = 'I'
                    
                    if cur == '-':
                        next # never need to do anything for these
                    
                    zero_width = ['7F', 'JL', 'F7', '7F', '|F', '|L']
                    corners = ['J','F','L','7']
                    #zigzag = ['FJ', 'L7']

                    if cur == 'L' or cur == 'F': # left-hand corners
                        left_corner = cur

                    if prev_tile in inside: 
                        next_nonpath = 'O'
                    elif prev_tile in outside:
                        next_nonpath = 'I'
                    # lots of cases for adjacent corners
                    elif cur_and_prev in zero_width:
                        next_nonpath = Pipes.swap_next(next_nonpath)
                    elif cur == '|':
                        next_nonpath = Pipes.swap_next(next_nonpath)
                    elif cur == 'J':
                        if left_corner == 'F':
                            next
                        else:
                            next_nonpath = Pipes.swap_next(next_nonpath)
                    elif cur == '7':
                        if left_corner == 'L':
                            next
                        else:
                            next_nonpath = Pipes.swap_next(next_nonpath)
                        
                    # elif cur in corners:
                    #     next_nonpath = Pipes.swap_next(next_nonpath)
                foo = True   
                    
        self.layout[start_row] = self.layout[start_row][:start_col] + 'S' + self.layout[start_row][start_col+1:]
        


        self.inside = inside
        self.outside = outside

        return len(inside)

    def swap_next(next):
        if next == 'O':
            return 'I'
        else:
            return 'O'            


    def get_left_right(dir):
        if dir == 'N':
            return ['W','E'] 
        elif dir == 'E':
            return ['N','S']
        elif dir == 'S':
            return ['E','W']
        elif dir == 'W':
            return ['S','N']
        
    def get_adj(self, node, dir):
        (row,col) = node
        if dir == 'N':
            adj = [row - 1, col]
            if adj[0] == -1:
                return []
        elif dir == 'S':
            adj = [row + 1, col]
            if adj[0] == self.height:
                return []
        elif dir == 'W':
            adj = [row, col - 1]
            if adj[1] == -1:
                return []
        elif dir == 'E':
            adj = [row, col + 1]
            if adj[1] == self.width:
                return []
        return adj
    
    def get_start_tile(self):
        # get two tiles adjacent to start
        before = self.path[1]
        after = self.path[-2]
        start = self.path[0]
        ends = []
        if before[0] == start[0] and before[1] < start[1]:
            ends.append('W')
        elif before[0] == start[0] and before[1] > start[1]:
            ends.append('E')
        elif before[0] < start[0] and before[1] == start[1]:
            ends.append('N')
        elif before[0] > start[0] and before[1] == start[1]:
            ends.append('S')
        
        if after[0] == start[0] and after[1] < start[1]:
            ends.append('W')
        elif after[0] == start[0] and after[1] > start[1]:
            ends.append('E')
        elif after[0] < start[0] and after[1] == start[1]:
            ends.append('N')
        elif after[0] > start[0] and after[1] == start[1]:
            ends.append('S')

        ends.sort()
        if ends == ['E','N']:
            return 'L'
        elif ends == ['N','S']:
            return '|'
        elif ends == ['N','W']:
            return 'J'
        elif ends == ['E','S']:
            return 'F'
        elif ends == ['E','W']:
            return '-'
        elif ends == ['S','W']:
            return '7'

        
        


with open('input') as f:
    lines = [ i.strip() for i in f.readlines() ]

my_maze = Pipes(lines)

my_maze.traverse()

print(len(my_maze.path) // 2) # farthest away is half of the total length
print()
print(my_maze.get_area())
my_maze.print_maze()