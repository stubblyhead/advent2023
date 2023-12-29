from dataclasses import dataclass

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

workflows = {}

with open('testcase') as f:
    lines = f.read()

flow_list, part_list = lines.split('\n\n')
flow_list = flow_list.split()
part_list = part_list.split()

parts = []

for i in part_list:
    ratings = i.split(',')
    parts.append(Part(int(ratings[0][3:]),int(ratings[1][3:]),int(ratings[2][3:]),int(ratings[3][3:-1])))

for i in flow_list:
    label, rules = i.split('{')
    workflows[label] = rules[:-1].split(',')


