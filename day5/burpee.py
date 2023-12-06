f = open('testcase')

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
soil = {}  
fert = {}
water = {}
light = {}
temp = {}
humid = {}
loc = {}

to_plant = [ int(i) for i in to_plant.split() ]

for p in to_plant:  # need to pre-load each dict with previous things keys
    seeds[p] = p

for map in seed_soil.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):  # ${rng} times, conveniently starts at 0
        seeds[src + i] = dest + i  # src maps to dest

for s in seeds:
    soil[s] = s

for map in soil_fert.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):
        soil[src + i] = dest + i

for s in soil:
    fert[s] = s

for map in fert_water.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):
        fert[src + i] = dest + i

for f in fert:
    water[f] = f

for map in water_light.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):
        water[src + i] = dest + i

for w in water:
    light[w] = w

for map in light_temp.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):
        light[src + i] = dest + i

for l in light:
    temp[l] = l

for map in temp_humid.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):
        temp[src + i] = dest + i

for t in temp:
    humid[t] = t

for map in humid_loc.split('\n'):
    (dest, src, rng) = [ int(i) for i in map.split() ]
    for i in range(rng):
        humid[src + i] = dest + i
