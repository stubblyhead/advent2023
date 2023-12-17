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
        hash = get_hash(label)
