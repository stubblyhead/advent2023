from dataclasses import dataclass

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def sum(h):
        return h.x+h.m+h.a+h.s

workflows = {}

with open('input') as f:
    lines = f.read()

flow_list, part_list = lines.split('\n\n')
flow_list = flow_list.split()
part_list = part_list.split()

parts = []

for i in part_list:
    ratings = i.split(',')
    parts.append(Part(int(ratings[0][3:]),int(ratings[1][2:]),int(ratings[2][2:]),int(ratings[3][2:-1])))

for i in flow_list:
    label, rules = i.split('{')
    workflows[label] = rules[:-1].split(',')

def do_workflow(w, p):
    for r in w:
        if len(r) > 1 and r[1] == '<':
            cmp,dst = r.split(':')
            if getattr(p,cmp[0]) < int(cmp[2:]):
                if dst == 'R':
                    return 0
                elif dst == 'A':
                    return p.sum()
                else:
                    return dst
                
        elif len(r) > 1 and r[1] == '>':
            cmp,dst = r.split(':')
            if getattr(p,cmp[0]) > int(cmp[2:]):
                if dst == 'R':
                    return 0
                elif dst == 'A':
                    return p.sum()
                else:
                    return dst

        elif r == 'A':
            return p.sum()

        elif r == 'R':
            return

        else:
            return r      


accepted = 0

for i in parts:
    w = 'in'
    while type(w) is str:
        w = do_workflow(workflows[w], i)
    if type(w) == int:
        accepted += w

print(accepted)
