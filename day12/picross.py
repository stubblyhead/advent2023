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


def find_valid_range(pattern, springs):
    # returns a starting position for the given group of springs
    p = '[#\?]{' + str(springs[0]) + '}' 
    for s in springs[1:]:
        p = p + '[\.\?]+[#\?]{' + str(s) + '}' 


    reg = re.compile(p) 
    # at least the given number springs/unknowns, not followed by a known spring
    # remaining = len(pattern) - (space_needed - spring_count - 1) # need at least this many spaces left
    return [ m.start() for m in reg.finditer(pattern, overlapped=True) ]
    
def count_arrangements(pattern, springs):
    count = 1
    if len(springs) > 1:
        this_group = springs[0]
        space_needed = sum(springs) + (len(springs) - 1)
        positions = find_valid_range(pattern, springs)
        count = len(positions)
        for p in positions:
            sub_pattern = pattern[p + this_group + 1:]
            return count * count_arrangements(sub_pattern, springs[1:])
    else:
        positions = find_valid_range(pattern, springs)
        count *= len(positions)
        return count



for l in lines:
    (pattern, springs) = l.split(' ')
    springs = [ int(i) for i in springs.split(',') ]

    pattern = simplify_pattern(pattern,springs)
    
    print(count_arrangements(pattern, springs))
