line = '1212568077 333451605'

line = [ int(i) for i in line.split() ]
seed_line = line
to_plant = []

for i in range(0, len(seed_line), 2):
    for j in range(seed_line[i+1]):
        to_plant.append(seed_line[i] + j)


print(len(to_plant))
