class Hand:
    card_order = ( 'J', '2', '3', '4','5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A' )
    # J is now Joker, lowest ranked card

    def __init__(self, cards):
      self.cards = cards

    def get_type(self):
        histo = {'J':0}
        for c in self.cards:
            if histo.get(c):
                histo[c] += 1
            else:
                histo[c] = 1
        counts = list(histo.values())
        counts.sort()
        counts.reverse() # order histogram values from high to low
        temprank = 0
        if counts[0] == 5:  # 5 of a kind
            temprank = 7
        elif counts[0] == 4: # 4 of a kind
            temprank = 6
        elif counts[0] == 3:
            if counts[1] == 2:
                temprank = 5 # first is 3, second is 2 --> full house
            else:
                temprank = 4 # otherwise 3 of a kind
        elif counts[0] == 2:
            if counts[1] == 2:
                temprank = 3 # first and second are both 2 --> two pair
            else:
                temprank = 2 # otherwise single pair
        else:
            temprank = 1 # high card

        if histo['J'] == 4:
            return temprank + 1 # four J turns 4oaK to 5oaK
        elif histo['J'] == 3:
            return temprank + 2 # 3oaK to FH or FH to 5oaK
        elif histo['J'] == 2:
            return temprank + 2
        elif histo['J'] == 1:
            if temprank == 1 or temprank == 6:
                return temprank + 1
            else:
                return temprank + 2

        

    def __lt__(self, a):
        # self < a
        if self.get_type() < a.get_type():
            return True # self is weaker hand type than a
        elif self.get_type() > a.get_type():
            return False # self is stronger hand type than a
        else:
            # self and a are same hand type, so check each card
            for i in range(5):
                if Hand.card_order.index(self.cards[i]) < Hand.card_order.index(a.cards[i]):
                    return True  # self 
                elif Hand.card_order.index(self.cards[i]) > Hand.card_order.index(a.cards[i]):
                    return False
                
    def __gt__(self, a):
        # self > a
        if self.get_type() < a.get_type():
            return False # self is weaker hand type than a
        elif self.get_type() > a.get_type():
            return True # self is stronger hand type than a
        else:
            # self and a are same hand type, so check each card
            for i in range(5):
                if Hand.card_order.index(self.cards[i]) < Hand.card_order.index(a.cards[i]):
                    return False  # self 
                elif Hand.card_order.index(self.cards[i]) > Hand.card_order.index(a.cards[i]):
                    return True



with open('testcase') as f:
    lines = f.readlines()

hands = {}
for h in lines:
    (c, v) = h.split()
    hands[Hand(c)] = int(v)

sorted_hands = list(hands.keys())
sorted_hands.sort()
winnings = 0

for h in range(len(sorted_hands)):
    bid = hands[sorted_hands[h]]
    winnings += (h+1)*bid

print(winnings)


