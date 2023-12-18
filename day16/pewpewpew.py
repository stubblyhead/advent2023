from dataclasses import dataclass, field

@dataclass
class Space:
    tile: str
    beams: list = field(default_factory = list)
    beam_count: int = 0

class Grid:
    def __init__(self, layout):
        self.layout = []
        self.beam_paths = [ [0,0,'R'] ]  # one path to start with, beginning at upper left and moving to the right
        self.layout[0][0].beam_count = 1
        for i in layout:
            i = i.strip()
            this_row = []
            for j in i:
                this_row.append(Space(j))
            self.layout.append(this_row)
        self.height = len(self.layout)
        self.width = len(self.layout[0])
        self.layout[0][0].beams.append('R')  # this might be useful later, not sure yet

    def shine(self):
        while self.beam_paths:  # going to assume every path will eventually exit the grid
            to_remove = []  # need to keep track during each tick to not change array length in mid-stream
            to_add = []  # same as above
            for i in len(self.beam_paths):
                p = self.beam_paths[i]
                # move each beam in the given direction
                if p[2] == 'U':
                    p[0] -= 1
                elif p[2] == 'D':
                    p[0] += 1
                elif p[2] == 'R':
                    p[1] += 1
                elif p[2] == 'L':
                    p[1] -= 1
                
                if p[0] == -1 or p[0] == self.width \
                or p[1] == -1 or p[1] == self.height:
                    to_remove.append(i)  # mark for removal from list
                    next   # move to the next beam
                else:
                    self.layout[p[0]][p[1]] += 1  # add 1 to beam count for this tile
                                    
                # mirrors 
                if self.layout[p[0]][p[1]] == '/':
                    if p[2] == 'U':
                        p[2] = 'R'
                    elif p[2] == 'D':
                        p[2] = 'L'
                    elif p[2] == 'R':
                        p[2] = 'U'
                    elif p[2] == 'L':
                        p[2] = 'D'
                elif self.layout[p[0]][p[1]] == '\\':
                    if p[2] == 'U':
                        p[2] = 'L'
                    elif p[2] == 'D':
                        p[2] = 'R'
                    elif p[2] == 'R':
                        p[2] = 'D'
                    elif p[2] == 'L':
                        p[2] = 'U'

                #splitters
                elif self.layout[p[0]][p[1]] == '-':
                    if p[2] == 'U' or p[2] == 'D':
                        p[2] = 'R'  # change direction on one beam...
                        to_add.append(list(p))
                        to_add[-1][2] == 'L'  # ... and add another beam going in the opposite direction
                elif self.layout[p[0]][p[1]] == '|':
                    if p[2] == 'L' or p[2] == 'R':
                        p[2] = 'U'
                        to_add.append(list(p))
                        to_add[-1][2] == 'D'

            to_remove.sort()
            to_remove.reverse() # need to remove from the beam list working backwards or else everything gets fucked up
            for i in to_remove:
                self.beam_paths.pop(i) # pop out item i

            self.beam_paths += to_add  # add new beams on the end


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