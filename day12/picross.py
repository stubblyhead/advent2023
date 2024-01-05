with open('testcase') as f:
    lines = [ i.strip() for i in f.readlines() ]

def check_line(line, groups):
    valid = 0
    if len(line) == 0 and len(groups) == 0:
        return 1
    elif len(line) == 0 and len(groups) > 0:
        return 0
    
    if line[0] == '.':
        return(check_line(line[1:], groups))
    elif line[0] == '?':
        return(check_line('#'+line[1:], groups) + check_line('.'+line[1:], groups))
    elif line[0] == '#':
        if len(groups) == 0:
               return 0
        else:
            if line[0:groups[0]].count('.') > 0:
                return 0
            if line[groups[0]] == '#':
                return 0
            if line[groups[0]] == '.':
                groups.pop(0)
                return check_line(line[groups[0]+1], groups)




