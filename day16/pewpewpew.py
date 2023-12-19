from dataclasses import dataclass, field

@dataclass
class Space:
    tile: str
    beams: list = field(default_factory = list)
    beam_count: int = 0

class Beam:
    def __init__(self, row, col, dir):
        self.row = [row]
        self.col = [col]
        self.dir = [dir]

    def add_step(self, row, col, dir):
        self.row.append(row)
        self.col.append(col)
        self.dir.append(dir)

    def get_current(self):
        return [self.row[-1], self.col[-1], self.dir[-1]]

    def contains(self, row, col, dir):
        for i in len(self.row):
            if self.row[i] == row and self.col[i] == col and self.dir[i] == dir:
                return True
        return False

class Grid:
    def __init__(self, layout):
        self.layout = []
        self.beam_paths = [ Beam(0, 0, 'R') ]  # one path to start with, beginning at upper left and moving to the right
        for i in layout:
            i = i.strip()
            this_row = []
            for j in i:
                this_row.append(Space(j))
            self.layout.append(this_row)
        self.layout[0][0].beam_count = 1
        self.height = len(self.layout)
        self.width = len(self.layout[0])
        self.layout[0][0].beams.append('R')  # this might be useful later, not sure yet

    def shine(self):
        while self.beam_paths:  # not every beam will exit the grid, some will loop around forever
            to_remove = []  # need to keep track during each tick to not change array length in mid-stream
            to_add = []  # same as above
            for i in range(len(self.beam_paths)):
                p = self.beam_paths[i]
                (row,col,dir) = p.get_current()
                # move each beam in the given direction
                if p.dir[-1] == 'U':
                    new_row = p.row[-1] - 1
                    if p.contains(new_row, row, dir): # if we've already been to this tile moving in this direction we're in a loop and can stop stepping through this one
                        to_remove.append(i)
                        continue
                    p.add_step(new_row, col, dir)
                elif p.dir[-1] == 'D':
                    new_row = p.row[-1] + 1
                    if p.contains(new_row, row, dir):
                        to_remove.append(i)
                        continue
                    p.add_step(new_row, col, dir)
                elif p.dir[-1] == 'R':
                    new_col = p.col[-1] + 1
                    if p.contains(row, new_col, dir):
                        to_remove.append(i)
                        continue
                    p.add_step(row, new_col, dir)
                elif p.dir[-1] == 'L':
                    new_col = p.col[-1] - 1
                    if p.contains(row, new_col, dir):
                        to_remove.append(i)
                        continue
                    p.add_step(row, new_col, dir)
    
                
                if p.row[-1] == -1 or p.row[-1] == self.height \
                or p.col[-1] == -1 or p.col[-1] == self.width:
                    to_remove.append(i)  # mark for removal from list
                    continue   # move to the next beam
                else:
                    self.layout[p.row[-1]][p.col[-1]].beam_count += 1  # add 1 to beam count for this tile
                                    
                # mirrors 
                if self.layout[p.row[-1]][p.col[-1]].tile == '/':
                    if p.dir[-1] == 'U':
                        p.dir[-1] = 'R'
                    elif p.dir[-1] == 'D':
                        p.dir[-1] = 'L'
                    elif p.dir[-1] == 'R':
                        p.dir[-1] = 'U'
                    elif p.dir[-1] == 'L':
                        p.dir[-1] = 'D'
                elif self.layout[p.row[-1]][p.col[-1]].tile == '\\':
                    if p.dir[-1] == 'U':
                        p.dir[-1] = 'L'
                    elif p.dir[-1] == 'D':
                        p.dir[-1] = 'R'
                    elif p.dir[-1] == 'R':
                        p.dir[-1] = 'D'
                    elif p.dir[-1] == 'L':
                        p.dir[-1] = 'U'

                #splitters
                elif self.layout[p.row[-1]][p.col[-1]].tile == '-':
                    if p.dir[-1] == 'U' or p.dir[-1] == 'D':
                        p.dir[-1] = 'R'  # change direction on one beam...
                        to_add.append(Beam(p.row[-1], p.col[-1], 'L'))   # ... and add another beam going in the opposite direction
                elif self.layout[p.row[-1]][p.col[-1]].tile == '|':
                    if p.dir[-1] == 'L' or p.dir[-1] == 'R':
                        p.dir[-1] = 'U'
                        to_add.append(Beam(p.row[-1], p.col[-1], 'D'))
                
                

            to_remove.sort()
            to_remove.reverse() # need to remove from the beam list working backwards or else everything gets fucked up
            for i in to_remove:
                self.beam_paths.pop(i) # pop out item i

            self.beam_paths += to_add  # add new beams on the end
            print(len(self.beam_paths))


with open('testcase') as f:
    lines = f.readlines()

my_grid = Grid(lines)

my_grid.shine()

energized = 0
for i in my_grid.layout:
    for j in i:
        if j.beam_count > 0:
            energized += 1

print(energized)