class Hand:
    def __init__(self, cards):
      self.cards = cards

    def get_type(self):
        histo = {}
        for c in self.cards:
            if histo.get(c):
                histo[c] += 1
            else:
                histo[c] = 1
        counts = list(histo.values())
        counts.sort()
        counts.reverse() # order histogram values from high to low
        if counts[0] == 5:  # 5 of a kind
            return 7
        elif counts[0] == 4: # 4 of a kind
            return 6
        elif counts[0] == 3:
            if counts[1] == 2:
                return 5 # first is 3, second is 2 --> full house
            else:
                return 4 # otherwise 3 of a kind
        elif counts[0] == 2:
            if counts[1] == 2:
                return 3 # first and second are both 2 --> two pair
            else:
                return 2 # otherwise single pair
        else:
            return 1 # high card

        


with open('testcase') as f:
    lines = f.readlines()

for h in lines:
    this_hand = Hand(h.split()[0])
    hand_type = this_hand.get_type()
    print(this_hand.cards, this_hand.get_type())


