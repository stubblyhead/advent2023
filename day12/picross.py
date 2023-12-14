import regex as re

with open('testcase') as f:
    lines = [ i.strip() for i in f.readlines() ]
    

totalcount = 0

def find_springs(pattern, springs):
    # if a ? must be a # to satisfy conditions, update it as such
    left = pattern
    for i in range(len(springs)):
        this_length = springs[i]
        start_pos = find_valid_range(pattern,springs[i])
        for j in range(start_pos,start_pos + this_length):
            left = left[:j] + str(i) + left[j+1:]
        left = left[0:this_length] + find_springs(left[this_length:],springs[i+1:])

    return left


def find_valid_range(pattern, spring_count):
    # returns a starting position for the given group of springs
    reg = re.compile('[#\?]{' + str(spring_count) + '}')

    return reg.search(pattern).start()



for l in lines:
    (pattern, springs) = l.split(' ')
    springs = [ int(i) for i in springs.split(',') ]

    find_springs(pattern,springs)
    # knock out the easy ones, not sure how I'm going to approach a general case


    # if len(pattern) == sum(springs) + len(springs) - 1:
    #     totalcount += 1  # need enough spaces for each group plus one space in between each

