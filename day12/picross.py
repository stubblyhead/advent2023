import regex as re

with open('testcase') as f:
    lines = [ i.strip() for i in f.readlines() ]
    

totalcount = 0

def simplify_pattern(pattern, springs):
    # if a ? must be a # to satisfy conditions, update it as such

    compact = ''  # spring patterns in as little space as possible
    locks = []  # list of spaces that have to be a spring
    for i in range(len(springs)):
        for j in range(springs[i]):
            compact += str(i)
        compact += '.'
    compact = compact[:-1] # don't need the final .
    left = compact.ljust(len(pattern), '.')
    right = compact.rjust(len(pattern), '.')

    for i in range(len(left)):
        if left[i].isdigit() and left[i] == right[i]:
            locks.append(i)

    simple = ''
    for i in range(len(pattern)):
        if i in locks:
            simple += '#'
        else:
            simple += pattern[i]
    return simple




def find_valid_range(pattern, spring_count, space_needed):
    # returns a starting position for the given group of springs
    reg = re.compile('[#\?]{' + str(spring_count) + ',}[^#]') 
    # at least the given number springs/unknowns, not followed by a known spring
    remaining = len(pattern) - (space_needed - spring_count - 1) # need at least this many spaces left
    return [ m.start() for m in reg.finditer(pattern, overlapped=True, endpos=remaining) ]
    



for l in lines:
    (pattern, springs) = l.split(' ')
    springs = [ int(i) for i in springs.split(',') ]

    pattern = simplify_pattern(pattern,springs)
    
    
    # if len(pattern) == sum(springs) + len(springs) - 1:
    #     totalcount += 1  # need enough spaces for each group plus one space in between each

