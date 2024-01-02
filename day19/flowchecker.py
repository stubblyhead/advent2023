import regex as re

with open('input') as f:
    lines = f.read()

lines = lines[:lines.index('\n\n')]

workflows = lines.split()

for w in workflows:
    label = w[:w.index('{')]
    label_count = len(re.findall(f'[^\w]({label})[^\w]',lines))
    # if label_count > 2:
    print(f'{label} {label_count}')