with open('input') as f:
    lines = f.readlines()

def get_diffs(s):
    diffs = []
    for i in range(len(s)-1):
        diffs.append(s[i+1] - s[i])
    return diffs

sum = 0

for seq in lines:
    seq = [ int(i) for i in seq.split() ]
    layers = [seq]
    while True:  # don't know how many times we need to do it, remember to break out at some point
        next_layer = get_diffs(layers[-1])
        layers.append(next_layer)
        if next_layer.count(0) == len(next_layer):  # if it's all zeros we're done
            break
    layers.pop(-1)  # zeros are extraneous, but will probably be significant later
    layers.reverse()
    for i in range(len(layers)):
        if i == len(layers) - 1:
            sum += layers[i][-1]  # original sequence should have the next number appended
        else:
            layers[i+1].append(layers[i+1][-1] + layers[i][-1])
print(sum)

sum = 0
for seq in lines: # could probably do this in a single loop but whatevs
    # will be mostly the same until towards the end
    seq = [ int(i) for i in seq.split() ]
    layers = [seq]
    while True:  # don't know how many times we need to do it, remember to break out at some point
        next_layer = get_diffs(layers[-1])
        layers.append(next_layer)
        if next_layer.count(0) == len(next_layer):  # if it's all zeros we're done
            break
    layers.pop(-1)  # zeros are extraneous, but will probably be significant laterz
    layers.reverse()
    for i in range(len(layers)):
            if i == len(layers) - 1:
                sum += layers[i][0] 
            else:
                layers[i+1].insert(0, layers[i+1][0] - layers[i][0])

print(sum)
