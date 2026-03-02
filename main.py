import deck

def test():

    # initiallize deck
    testDeck = deck.Deck()
    print("Deck: ", end="")
    testDeck.showDeck()
    print("")

    # deal hand
    testDeck.shuffle()
    hand = testDeck.deal(5)

    # print hand
    print("Hand: [", end="")
    for i in range(len(hand)):
        hand[i].show("")
        if (i < len(hand) - 1): print(", ", end ="")
    print("]\n")

    print("Deck: ", end="")
    testDeck.showDeck()

def main():
    test()

if __name__ == "__main__":
    main()
