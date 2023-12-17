with open('input') as f:
    steps = [ i for i in f.readline().split(',') ]


hash = 0

for s in steps:
    for l in s:
        hash += ord(l)
        hash *= 17
        hash %= 256

print(hash)