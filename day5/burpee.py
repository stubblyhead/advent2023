class Map:
    # create object for each line of mappings
    def __init__(self, map_line):
        (dest,src,rng) = [ int(i) for i in map_line.split() ]
        self.dest = dest
        self.src = src
        self.rng = rng
        
    def convert(self, src):
        # if source value is in this mapping return the correpsonding destination value,
        # otherwise return -1
        if src in range(self.src, self.src + self.rng):
            return src - self.src + self.dest
        else:
            return -1

f = open('input')

parts = f.read().split('\n\n')
to_plant = parts[0].split(': ')[1]
seed_soil = parts[1].split(':\n')[1]
soil_fert = parts[2].split(':\n')[1]
fert_water = parts[3].split(':\n')[1]
water_light = parts[4].split(':\n')[1]
light_temp = parts[5].split(':\n')[1]
temp_humid = parts[6].split(':\n')[1]
humid_loc = parts[7].split(':\n')[1]

# each hash maps current type to next type
seeds = {}  # is this a good idea?  time will tell!
soil = {}   # narrator: it was not
fert = {}
water = {}
light = {}
temp = {}
humid = {}
loc = {}

to_plant = [ int(i) for i in to_plant.split() ]

