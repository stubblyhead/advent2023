lines = open('testcase').readlines(-1)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

valid_count = 0

for l in lines:
    is_valid = True
    parts = l.strip().split(': ')
    game_num = int(parts[0].split(' ')[1])
    draws = parts[1].split('; ')
    for d in draws:
        counts = d.split(', ')
        for c in counts:
            dice = c.split(' ')
            if dice[1] == 'red' and int(dice[0]) > MAX_RED:
                is_valid = False
            if dice[1] == 'green' and int(dice[0]) > MAX_GREEN:
                is_valid = False
            if dice[1] == 'blue' and int(dice[0]) > MAX_BLUE:
                is_valid = False
    if is_valid:
        valid_count += game_num

print(valid_count)
