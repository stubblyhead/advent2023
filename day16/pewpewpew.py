from dataclasses import dataclass, field

@dataclass
class Space:
    tile: str
    beams: list = field(default_factory = list)

class Grid:
    def __init__(self, layout):
        self.layout = []
        for i in layout:
            this_row = []
            for j in i:
                this_row.append(Space(j))
            self.layout.append(this_row)


