with open('input') as f:
    patterns = f.read().split('\n\n')

def check_reflection(pattern):
    for i in range(1,len(pattern)):
        above = pattern[:i] # split pattern into groups above and below each interstice
        below = pattern[i:]
        above.reverse() # will make it easier to iterate through them together
        mirror = True # assume match until we prove otherwise
        if len(above) < len(below):
            for j in range(len(above)):
                if above[j] == below[j]:
                    next
                else:
                    mirror = False # found rows that don't match...
                    break # ...so we don't need to keep checking this possible reflection
        else:
            for j in range(len(below)):
                if above[j] == below[j]:
                    next
                else:
                    mirror = False
                    break
        if mirror:
            return i
      
    return -1  # got all the way through and didn't find a reflection

def fix_smudge(pattern):
    for i in range(1,len(pattern)):
        above = pattern[:i] # starts off pretty much the same
        below = pattern[i:]
        above.reverse()
        one_off = True
        if len(above) < len(below):
            for j in range(len(above)):
                if above[j] == below[j]:
                    next
                elif compare_lines(above[j], below[j]):
                    next
                else:
                    one_off = False
                    break
        if one_off:
            return i
    return -1

def compare_lines(a, b):
    # return True if there's a single character different, otherwise False
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            if diff > 1:
                return False  # no need to keep checking if there's more than 1
    if diff == 1:
        return True
    else:  # shouldn't ever get here, but probably should do this
        raise ValueError  

part_one_total = 0
part_two_total = 0
for p in patterns:
    p = p.split()
    tpose = []
    for i in range(len(p[0])):
        tpose.append( [ l[i] for l in p ] )

    h = check_reflection(p)
    if h > 0:
        part_one_total += 100 * h
        next
    else:
        v = check_reflection(tpose)
        part_one_total += v

    h = fix_smudge(p)
    if h > 0:
        part_two_total += 100 * h
    else:
        v = fix_smudge(tpose)
        part_two_total += v

print(part_one_total)
print(part_two_total)
