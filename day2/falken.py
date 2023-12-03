lines = open('input').readlines(-1)

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

total_power = 0

for l in lines:
    min_red = 0
    min_green = 0
    min_blue = 0
    parts = l.strip().split(': ')
    draws = parts[1].split('; ')
    for d in draws:
        colors = d.split(', ')
        for c in colors:
            (count,color) = c.split(' ')
            if color == 'red':
                #minimum color needed is max of previous min and current count
                min_red = max(min_red, int(count)) 
            elif color == 'blue':
                #do it for every color
                min_blue = max(min_blue, int(count))
            elif color == 'green':
                min_green = max(min_green, int(count))
    total_power += min_red * min_green * min_blue

print(total_power)