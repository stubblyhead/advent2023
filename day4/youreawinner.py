from collections import defaultdict
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

# this is the dumbest lottery ever
cardcounts = defaultdict(int)
for i in range(len(lines)):
    card = lines[i]
    (winners, picks) = card.split(' | ')
    winners = winners.split(': ')[1].strip().split()
    picks = picks.strip().split()
    matches = 0
    cardcounts[i] += 1 # always add one for the original card
    for p in picks:
        if p in winners:
            matches += 1
    if matches > 0:
        for j in range(i + 1, i + matches + 1):  # for the ${matches} next cards...
            cardcounts[j] += cardcounts[i]  # ... add equal to the count of the current card

print(sum(cardcounts.values()))
