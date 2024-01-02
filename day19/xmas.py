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

with open('testcase') as f:
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
        self.count = self.max - self.min + 1

    def __eq__(self, b):
        if self.min == b.min and self.max == b.max:
            return True
        else:
            return False

    # def __truediv__(self, b):
    #     if self == b:
    #         return self
    #     else:
    #         if self.min == b.min:
    #             self.min = b.max + 1
    #         elif self.max == b.max:
    #             self.max = b.min - 1
        
    #     return PartRange(self.min, self.max)

x = PartRange()
m = PartRange()
a = PartRange()
s = PartRange()

flow_queue = SimpleQueue()
flow_queue.put(['in',x,m,a,s])
valid = 0

while not flow_queue.empty():
    (flow,x,m,a,s) = flow_queue.get()
    rules = workflows[flow]
    dest_flows = []
    
    for r in rules:
        new_x = PartRange(x.min,x.max)
        new_m = PartRange(m.min,m.max)
        new_a = PartRange(a.min,a.max)
        new_s = PartRange(s.min,s.max)
        if r.find(':') >= 0:
            cmp,dest = r.split(':')
        else:
            dest = r
            cmp = ''
        if cmp.find('>') > 0:
            q,n = cmp.split('>')
            n = int(n)
            locals()['new_'+q] = PartRange(n+1,locals()[q].max)
            locals()[q] = PartRange(locals()[q].min, n)
            
        elif cmp.find('<') > 0:
            q,n = cmp.split('<')
            n = int(n)
            locals()['new_'+q] = PartRange(locals()[q].min, n-1)
            locals()[q] = PartRange(n,locals()[q].max)
            
        if dest == 'A':
            valid += (new_x.count * new_m.count * new_a.count * new_s.count)
        elif dest != 'R':
            flow_queue.put([dest,new_x,new_m,new_a,new_s])
            # x /= new_x
            # m /= new_m
            # a /= new_a
            # s /= new_s

            
print(valid)