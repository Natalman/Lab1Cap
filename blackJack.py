import random
def main():
    deck = create_deck()
    players =  2
    hand =0
    scores = []

    for player in range(players):
        hand1 = deal_cards(deck, hand)
        hand2 = deal_cards(deck, hand1)
        scores.append(hand2)

    print(scores[0])
    print(scorees[1])

    while True:
        scores[0] = deal_cards(deck, scores[0])
        print(scores[0])
        scores[1] = deal_cards(deck, scores[1])
        print(scores[1])

        if scores[0] > 21:
            print('Player 1: You have lost')
            break

        elif scores[0] == 21:
            print ('Player 1: You have won')
            break

        scores[1] = deal_cards(deck, scores[1])
        print (scores[1])

        if scores[0] > 21 or scores[1] > 21:
            print('Player 2: You have lost')
            break
        elif scores[0] == 21 or scores[1] == 21:
            print ('player 2: You have won')
            break

def create_deck():
    deck = {'Ace of spades': 1, '2 of spades': 2, '3 of spades': 3,
            '4 of spades': 4, '5 of spades': 5, '6 of spades': 6, '7 of spades': 7,
            '8 of spades': 8, '9 of spades': 9, '10 of spades': 10, 'Jack of spades': 10,
            'Queen of spades': 10, 'King of spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7,
            '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of clubs': 1, '2 of clubs': 2, '3 of clubs': 3,
            '4 of clubs': 4, '5 of clubs': 5, '6 of clubs': 6, '7 of clubs': 7,
            '8 of clubs': 8, '9 of clubs': 9, '10 of clubs': 10, 'Jack of clubs': 10,
            'Queen of clubs': 10, 'King of clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7,
            '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
            'Jack of Diamonds': 10,'Queen of Diamonds': 10, 'King of Diamonds': 10}
    return deck

def deal_cards(deck, hand_value):
    randCard = deck.popitem()
    card = randCard[0]
    value = randCard[1]
    print(card)

    if("Ace" in card):
        ace = input('Would you like it to be 11 or 1?')
        if(ace =="11"):
            value = 11
    hand_value+=value
