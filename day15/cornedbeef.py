with open('input') as f:
    steps = [ i for i in f.readline().split(',') ]


hash_sum = 0

for s in steps:
    hash = 0
    for l in s:
        hash += ord(l)
        hash *= 17
        hash %= 256
    hash_sum += hash

print(hash_sum)