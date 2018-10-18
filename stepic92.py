import collections

NUMERAL_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

cardsss = "10C JC QC KB AC"


# card_list = [str(x) for x in input().split()]
card_list = [str(x) for x in cardsss.split()]

# print(card_list)


short_desc = "High Card"
numeral_dict = collections.defaultdict(int)
suit_dict = collections.defaultdict(int)
for my_card in card_list:
    numeral_dict[my_card[:-1]] += 1
    suit_dict[my_card[-1]] += 1

print(numeral_dict.items(), suit_dict.items())


# Pair
if len(numeral_dict) == 4:
    short_desc = "One pair"
# Two pair or 3-of-a-kind
elif len(numeral_dict) == 3:
    if 3 in numeral_dict.values():
        short_desc = "Three of a kind"
    else:
        short_desc = "Two pairs"
# Full house or 4-of-a-kind
elif len(numeral_dict) == 2:
    if 2 in numeral_dict.values():
        short_desc = "Full house"
    else:
        short_desc = "Four of a kind"
else:
    # Flushes and straights
    straight, flush, royal = False, False, False
    if len(suit_dict) == 1:
        flush = True
    min_numeral = min([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
    max_numeral = max([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
    if int(max_numeral) - int(min_numeral) == 4:
        straight = True
    # Ace can be low
    low_straight = set(("A", "2", "3", "4", "5"))
    royal_straight = set(("A", "K", "Q", "J", "10"))
    if not set(numeral_dict.keys()).difference(low_straight):
        straight = True
    if straight and not flush:
        short_desc = "Straight"
    elif flush and not straight:
        short_desc = "Flush"
    elif flush and straight:
        short_desc = "Straight flush"
    if not set(numeral_dict.keys()).difference(royal_straight) and flush:
        short_desc = "Royal flush"


print(short_desc)
