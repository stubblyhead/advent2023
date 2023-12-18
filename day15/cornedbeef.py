from dataclasses import dataclass

with open('input') as f:
    steps = [ i for i in f.readline().split(',') ]


@dataclass
class Lens:
    label: str
    focal_length: int

def get_hash(val):
    hash = 0
    for c in val:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash

hash_sum = 0

for s in steps:
    hash_sum += get_hash(s)

print(hash_sum)

boxen = [ [] for i in range(256) ] # create list with 256 elements
for s in steps:
    if s[-1].isnumeric():
        (label, length) = s.split('=')
        length = int(length)
        hash = get_hash(label)
        updated = False
        for i in boxen[hash]:
            if i.label == label:
                i.focal_length = length
                updated = True  # updated lens w/ existing labe
                break
        if not updated: # if there wasn't already a lens with this label...
            boxen[hash].append(Lens(label, length)) # ...add one onto the end of the list

    else:
        label = s[:-1]
        hash = get_hash(label)
        for i in range(len(boxen[hash])):
            if boxen[hash][i].label == label:  # if this label exists in this box...
                boxen[hash].pop(i) # ... pop it out of the list, moving everything else up
                break

power = 0

for i in range(len(boxen)):
    for j in range(len(boxen[i])):
        power += ((i+1) * (j+1) * boxen[i][j].focal_length)

print(power)

            