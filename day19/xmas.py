from dataclasses import dataclass
from queue import SimpleQueue

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

@dataclass
class PartRange():
    min: int = 1
    max: int = 4000

    def __post_init__(self):
        count = max - min + 1

x = PartRange()
m = PartRange()
a = PartRange()
s = PartRange()

flow_queue = SimpleQueue()
flow_queue.put(['in',x,m,a,s])
valid = 0

while not flow_queue.empty():
    (flow,x,m,a,s) = flow_queue.get()
    new_x = PartRange(x.min,x.max)
    new_m = PartRange(m.min,m.max)
    new_a = PartRange(a.min,a.max)
    new_s = PartRange(s.min,s.max)
    rules = workflows[flow]
    dest_flows = []
    
    for r in rules:
        if r.find(':') >= 0:
            cmp,dest = r.split(':')
        else:
            dest = r
        if cmp.find('>') > 0:
            q,n = cmp.split('>')
            n = int(n)
            locals()[q] = PartRange(locals()[q].min, n)
            locals()['new_'+q] = PartRange(n+1,locals()['new_'+q].max)
        elif cmp.find('<') > 0:
            q,n = cmp.split('<')
            n = int(n)
            locals()[q] = PartRange(locals()[q].min, n-1)
            locals()['new_'+q] = PartRange(n,locals()['new_'+q].max)

            
        if dest == 'A':
            True
        elif dest != 'R':
            flow_queue.put(dest)
            dest_flows.append(dest)
    if len(dest_flows) == 0:
        print(workflows[flow])
