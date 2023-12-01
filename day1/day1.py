import re

lines = open('input').readlines(-1)
calsum = 0

for l in lines:
    pattern = re.compile('\d')
    digits = pattern.findall(l)
    calsum += int(digits[0]) * 10 + int(digits[-1])

print(calsum)
    
