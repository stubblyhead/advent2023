import regex as re

with open('testcase') as f:
    lines = [ i.strip() for i in f.readlines() ]
    

totalcount = 0

def simplify_pattern(pattern, springs):
    # if a ? must be a # to satisfy conditions, update it as such

    left = right = ''
    for i in range(len(springs)):
        for j in range(springs[i]):
            left += str(i)
        left += '.'

    if len(left) > len(pattern):
        left = left[0:len(pattern)]
    print(left)



def find_valid_range(pattern, spring_count):
    # returns a starting position for the given group of springs
    reg = re.compile('[#\?]{' + str(spring_count) + ',}^#') 
    # at least the given number springs/unknowns, not followed by a known spring

    return reg.search(pattern).start()



for l in lines:
    (pattern, springs) = l.split(' ')
    springs = [ int(i) for i in springs.split(',') ]

    simplify_pattern(pattern,springs)
    # knock out the easy ones, not sure how I'm going to approach a general case


    # if len(pattern) == sum(springs) + len(springs) - 1:
    #     totalcount += 1  # need enough spaces for each group plus one space in between each

