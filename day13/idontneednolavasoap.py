with open('input') as f:
    patterns = f.read().split('\n\n')

def check_horiz(pattern):
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
            return 100 * i
      
    return -1  # got all the way through and didn't find a reflection

def check_vert(pattern):
    # easier to transpose once at the start than do it in each iteration
    tmp = []
    for i in range(len(pattern[0])):
        tmp.append( [ l[i] for l in pattern ] )
    
    pattern = tmp

    # now basically the same as before but with a different multiplier
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

total = 0
for p in patterns:
    p = p.split()

    h = check_horiz(p)
    if h > 0:
        total += h
        next
    else:
        v = check_vert(p)
        total += v

print(total)