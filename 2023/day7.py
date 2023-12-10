import sys
import re

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        hand_to_bid, hand_to_type  = {}, {}

        haindgh = []
        crds = set()
        for line in lines:
            cards, bid = line.split()
            haindgh.append(hand_key(cards, int(bid)))
            crds.add(cards)
        
        haindgh = sorted(haindgh)
        
        moneys = sum([(i+1)*hand[6] for i, hand in enumerate(haindgh)])
        print(f" Money: {moneys}")


def hand_key(orig_hand, bid):
    cards = ["J","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    card_to_value = {card: int(index + 1) for index, card in enumerate(cards)}
    card_to_value["J"] = 1
    hand = sorted(orig_hand)
    type_ = -1

    if hand[0] == hand[4]:
        type_ = 7 # 5 of a kind
    elif hand[0] == hand[3] or hand[1] == hand[4]:
        type_ = 6 # 4 of a kind
    elif hand[0] == hand[2] and hand[3] == hand[4] or hand[0] == hand[1] and hand[2] == hand[4]:
        type_ = 5 # full house
    elif hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
        type_ = 4 # 3 of a kind
    elif hand[0] == hand[1] and hand[2] == hand[3] or hand[0] == hand[1] and hand[3] == hand[4] or hand[1] == hand[2] and hand[3] == hand[4]:
        type_ = 3 # 2 pairs
    elif hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        type_ = 2 # 1 pair
    else:
        type_ = 1

    new_type_J = {1: {1: 2, 2: 4, 3: 5, 4: 6, 6: 7, 7: 7}, 2: {2: 4, 3: 6, 5:7}, 3: {4: 6, 5:7}, 4: {6:7}}
    type_ = new_type_J.get(hand.count("J"), {}).get(type_, type_)  #perform sustitution if there is a wildcard J

    return [type_ , *[card_to_value[card] for card in orig_hand], bid]

if __name__ == "__main__":
    main(sys.argv[1])