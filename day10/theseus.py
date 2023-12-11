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
                elif (i,j) in self.left_nodes:
                    c = "\033[94m" + c + "\033[0m"
                elif (i,j) in self.right_nodes:
                    c = "\033[92m" + c + "\033[0m"
                templine += c
            print(templine)

    def get_area(self):
        # get list of all points not on the path.  traverse the path, keeping track of
        # left vs right in first-person perspective.  left side and right side go in
        # separate arrays.  remove path points from both.  whichever one touches the
        # edge is outside, the other is inside.

        path = self.path
        layout = self.layout
        allpoints = [ (i,j) for i in range(len(layout)) for j in range(len(layout[i])) ]  # using a set here will make it easier to split things up later
        allpoints = set(allpoints)
        not_path = set()
        left_nodes = set()
        right_nodes = set()
        for p in allpoints:
            if p not in path:
                not_path.add(p)
        dir_of_travel = ''
        if path[1][0] > path[0][0]:
            dir_of_travel = 'S'
        elif path[0][0] > path[1][0]:
            dir_of_travel = 'N'
        elif path[1][1] > path[0][1]:
            dir_of_travel = 'E'
        elif path[0][1] > path[1][1]:
            dir_of_travel = 'W'
        for i in range(1,len(path)):
            p = path[i]
            prev = path[i-1]
            if p[0] > prev[0]:
                dir_of_travel = 'S'
            elif prev[0] > p[0]:
                dir_of_travel = 'N'
            elif p[1] > prev[1]:
                dir_of_travel = 'E'
            elif prev[1] > p[1]:
                dir_of_travel = 'W'

            (left_dir,right_dir) = Pipes.get_left_right(dir_of_travel)
            left = Pipes.get_adj(self, p, left_dir)
            right = Pipes.get_adj(self, p, right_dir)
            if left:
                left_nodes.add(tuple(left))
            if right:
                right_nodes.add(tuple(right))
            
        # remove path nodes from left and right
        left_nodes -= set(path)
        right_nodes -= set(path)
        self.left_nodes = left_nodes
        self.right_nodes = right_nodes
        # now need to figure out which is inside and which is outside
        for n in left_nodes:
            if n.count(0) > 0:
                return len(right_nodes)
            elif n[0] == self.height:
                return len(right_nodes)
            elif n[1] == self.width:
                return len(right_nodes)
            else:
                return len(left_nodes)

                


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
        
        


with open('input') as f:
    lines = [ i.strip() for i in f.readlines() ]

my_maze = Pipes(lines)

my_maze.traverse()

print(len(my_maze.path) // 2) # farthest away is half of the total length
print()
print(my_maze.get_area())
my_maze.print_maze()