import regex as re
import collections
lines = open('input').readlines(-1)
partsum = 0
gears = collections.defaultdict(list)
gearprod = 0

for i in range(len(lines)):
    cur = lines[i].strip()
    if i == 0:
        prev = ''
    else:
        prev = lines[i-1].strip()
    if i == len(lines)-1:
        next = ''
    else:
        next = lines[i+1].strip()
    pattern = re.compile('\d+')
    numbers = pattern.finditer(cur)  # find all numbers in each line
    for n in numbers:
        num = int(n.group()) # get the value
        start = n.start()  # where does each nubmer begin
        length = n.end() - start  # how long is it
        # border = ''
        left_edge = max(0,start-1)
        right_edge = min(start+length+1,len(cur)-1)
        above = prev[left_edge:right_edge]
        middle = cur[left_edge:right_edge]
        below = next[left_edge:right_edge]
        # border += prev[left_edge:right_edge] # get characters above number
        # border += next[left_edge:right_edge] # get chars below number
        # if start > 0:
        #     border += cur[start-1]
        # if start + length < len(cur):
        #     border += cur[start+length]
        # symbols = re.findall('[^\.\d]', border)  # check if surrounding chars have anything besides a period
        # if len(symbols) > 0:
        #     partsum += num  # if there's a symbol add to the tally


        # going to try doing this differently to make part 2 easier
        pattern = re.compile('[^\.\d]')
        if start == 0:  # not sure I understand why this is necessary, but it works
            offset = 0
        else:
            offset = 1
        symbols = pattern.search(above)
        if symbols:
            partsum += num
            if symbols.group() == '*':  # need to take note of where these are for later
                gears[(i-1,symbols.start()+start-offset)].append(num)

        symbols = pattern.search(middle)
        if symbols:
            partsum += num
            if symbols.group() == '*':
                gears[(i,symbols.start()+start-offset)].append(num)

        symbols = pattern.search(below)
        if symbols:
            partsum += num
            if symbols.group() == '*':
                gears[(i+1,symbols.start()+start-offset)].append(num)

print(partsum)
for parts in gears.values():
    if len(parts) == 2:
        gearprod += parts[0] * parts[1]

print(gearprod)
