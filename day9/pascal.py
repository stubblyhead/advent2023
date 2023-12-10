with open('testcase') as f:
    lines = f.readlines()

def get_diffs(seq):
    diffs = []
    seq.reverse()
    for i in range(len(seq)-1):
        diffs.append(seq[i] - seq[i+1])
    return diffs

seq = [ int(i) for i in lines[0].split() ]

print(get_diffs(seq))