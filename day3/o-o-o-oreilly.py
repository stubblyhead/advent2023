import regex as re
lines = open('testcase').readlines(-1)
partsum = 0

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
    numbers = pattern.findall(cur)  # find all numbers in each line
    for n in numbers:
        start = cur.index(n)  # where does each nubmer begin
        length = len(n)  # how long is it
        border = ''
        left_edge = max(0,start-1)
        right_edge = min(start+length+1,len(cur)-1)
        border += prev[left_edge:right_edge] # get characters above number
        border += next[left_edge:right_edge] # get chars below number
        if start > 0:
            border += cur[start-1]
        if start + length < len(cur):
            border += cur[start+length]
        symbols = re.findall('[^\.]', border)  # check if surrounding chars have anything besides a period
        if len(symbols) > 0:
            partsum += int(n)  # if there's a symbol add to the tally

print(partsum)