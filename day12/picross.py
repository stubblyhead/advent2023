from collections import defaultdict

with open('input') as f:
    lines = [ i.strip() for i in f.readlines() ]

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = defaultdict(str)
    def __call__(self, *args):
        import pickle
        s = pickle.dumps(args)
        if self.memo[s] == '':
            self.memo[s] = self.fn(*args)
        return self.memo[s]

def check_line(line, groups):
    if len(line) == 0 and len(groups) == 0:
        return 1  # no chars left in line, and all groups accounted for
    elif len(line) == 0 and len(groups) > 0:
        return 0  # no chars left, but some groups not allocated
    if len(line) < sum(groups) + len(groups) - 1:
        return 0  # not enough chars left regardless of type to fill all remaining groups

    if line[0] == '.':
        return(check_line(line[1:], groups)) # leading . can be disregarded, try again without it
    elif line[0] == '?':
        y = check_line('#'+line[1:], list(groups)) # could be either one, so have to check both
        n = check_line('.'+line[1:], list(groups))
        return(y+n)
    elif line[0] == '#':
        if len(groups) == 0:
               return 0  # hits still exist in line, but no groups to fill them with
        else:
            if line[0:groups[0]].count('.') > 0:
                return 0  # not enough consecutive # or ? to fill first group
            if line[0:groups[0]].count('.') == 0 and len(line) == groups[0]:
                g = groups.pop(0)  # this case is kind of dumb, should rework it
                return check_line(line[g:],groups)
            if line[groups[0]] == '#':
                return 0  # too many # or ? in a row, reject
            if line[groups[0]] == '.' or line[groups[0]] == '?':
                g = groups.pop(0)  # next char after group can be a space, strip it off and rerun
                return check_line(line[g+1:], groups)
            
check_line = Memoize(check_line)
total = 0
for l in lines:
    pattern, groupstr = l.split()
    groups = list(map(int, groupstr.split(',')))
    total += check_line(pattern, groups)

print(total)
big_total = 0
for l in lines:
    pattern, groupstr = l.split()
    groups = list(map(int, groupstr.split(',')))
    big_pattern, big_groups = pattern, groups
    for i in range(4):
        big_pattern = big_pattern + '?' + pattern
        big_groups = big_groups + groups
    big_total += check_line(big_pattern, big_groups)

print(big_total)