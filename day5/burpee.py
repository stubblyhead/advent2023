from copy import deepcopy

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
        
    def go_back(self, dest):
        if dest in range(self.dest, self.dest + self.rng):
            return dest - self.dest + self.src
        else:
            return -1

f = open('input')

parts = f.read().split('\n\n')
to_plant = parts[0].split(': ')[1]
seed_soil_lines = parts[1].split(':\n')[1]
soil_fert_lines = parts[2].split(':\n')[1]
fert_water_lines = parts[3].split(':\n')[1]
water_light_lines = parts[4].split(':\n')[1]
light_temp_lines = parts[5].split(':\n')[1]
temp_humid_lines = parts[6].split(':\n')[1]
humid_loc_lines = parts[7].split(':\n')[1]

# each hash maps current type to next type
seeds = {}  # is this a good idea?  time will tell!
soil = {}   # narrator: it was not
fert = {}
water = {}
light = {}
temp = {}
humid = {}
loc = {}

seed_soil = []
soil_fert = []
fert_water = []
water_light = []
light_temp = []
temp_humid = []
humid_loc = []

to_plant = [ int(i) for i in to_plant.split() ]

for l in seed_soil_lines.split('\n'):
    seed_soil.append(Map(l))

for l in soil_fert_lines.split('\n'):
    soil_fert.append(Map(l))

for l in fert_water_lines.split('\n'):
    fert_water.append(Map(l))

for l in water_light_lines.split('\n'):
    water_light.append(Map(l))

for l in light_temp_lines.split('\n'):
    light_temp.append(Map(l))

for l in temp_humid_lines.split('\n'):
    temp_humid.append(Map(l))

for l in humid_loc_lines.split('\n'):
    humid_loc.append(Map(l))

for i in to_plant:
    breakout = False
    for map in seed_soil:
        conv = map.convert(i)
        if conv > 0:
            seeds[i] = conv  
            breakout = True
            # if target seed is in this mapping then set the conversion value and move
            # to the next seed
        if breakout:
            break

        seeds[i] = i  # otherwise conversion value is the same

# now do the same thing six more times
for s in seeds.values():
    breakout = False
    for map in soil_fert:
        conv = map.convert(s)
        if conv > 0:
            soil[s] = conv
            breakout = True
        if breakout:
            break

        soil[s] = s
        
for s in soil.values():
    breakout = False
    for map in fert_water:
        conv = map.convert(s)
        if conv > 0:
            fert[s] = conv
            breakout = True
        if breakout:
            break

        fert[s] = s
        
for f in fert.values():
    breakout = False
    for map in water_light:
        conv = map.convert(f)
        if conv > 0:
            water[f] = conv
            breakout = True
        if breakout:
            break

        water[f] = f
        
for w in water.values():
    breakout = False
    for map in light_temp:
        conv = map.convert(w)
        if conv > 0:
            light[w] = conv
            breakout = True
        if breakout:
            break

        light[w] = w
        
for l in light.values():
    breakout = False
    for map in temp_humid:
        conv = map.convert(l)
        if conv > 0:
            humid[l] = conv
            breakout = True
        if breakout:
            break

        humid[l] = l

for h in humid.values():
    breakout = False
    for map in humid_loc:
        conv = map.convert(h)
        if conv > 0:
            loc[h] = conv
            breakout = True
        if breakout:
            break

        loc[h] = h

def find_lowest(maps, a):
    candidates = []
    for m in maps:
        candidates.append(m.go_back(a))
    if candidates.count(-1) == len(candidates):
        return a
    else:
        return max(candidates)

print(min(loc.values()))

seed_ranges = []
for i in range(0, len(to_plant), 2):
    seed_ranges.append(range(to_plant[i],to_plant[i]+to_plant[i+1]-1))
low_loc = 0
while True:
    low_humid = find_lowest(humid_loc, low_loc)
    low_temp = find_lowest(temp_humid, low_humid)
    low_light = find_lowest(light_temp, low_temp)
    low_water = find_lowest(water_light, low_light)
    low_fert = find_lowest(fert_water, low_water)
    low_soil = find_lowest(soil_fert, low_fert)
    low_seed = find_lowest(seed_soil, low_soil)
    for r in seed_ranges:
        if low_seed >= r.start and low_seed <= r.stop:
            print(low_loc)
            exit()
    low_loc += 1
    continue
        

