lines = open('input').readlines()
points = 0

for card in lines:
    # the card number will probably be significant in part 2
    (winners, picks) = card.split(' | ')
    winners = winners.split(': ')[1].strip().split()
    picks = picks.strip().split()
    matches = 0
    for p in picks:  # for each number in the picks...
        if p in winners: # ...increment matches if it's also in winners
            matches += 1
    if matches > 0:
        points += 2**(matches-1)

print(points)