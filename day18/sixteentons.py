with open('testcase') as f:
    lines = f.readlines()

dir = []
dist = []
color = []

for l in lines:
    i,j,k = l.strip().split()
    dir.append(i)
    dist.append(int(j))
    color.append(k[1:-1]) # assuming the parens don't matter

# need to figure out where the starting point even is
left = 0
right = 0
up = 0
down = 0
for i in range(len(dir)):
    if dir[i] == 'L':
        left += dist[i]
    elif dir[i] == 'R':
        right += dist[i]
    elif dir[i] == 'U':
        up += dist[i]
    else:
        down += dist[i]

print(f"from start there are {right} spaces to the right, {left} spaces to the left, {up} spaces above, and {down} spaces below" % right,left,up,down)