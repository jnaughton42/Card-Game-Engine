# Card and Deck class file
import random

class Card:
    
    def __init__(self, value, suit):
        self._suit = suit
        self._value = value
    
    def show(self, endBehavior = '\n'):
        print(f"{self._value} of {self._suit}", end = endBehavior)
        

class Deck:
    
    def __init__(self):
        self._cardList = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        self._cardList = [Card(v, s) for v in values for s in suits]
        
    def shuffle(self):
        random.shuffle(self._cardList)
        
    def showDeck(self):
        print("[", end="")
        counter = 0
        for card in self._cardList:
            counter += 1
            card.show("")
            if (counter != len(self._cardList)): print(", ", end="")
            if (counter % 7 == 0): print("")
        print("]")
        
    def remove(self, i):
        return self._cardList.pop(i)
        
    def insert(self, i, card):
        self._cardList.insert(i, card)
        
    def size(self):
        return len(self._cardList)
        
    def deal(self, num):
        hand = []
        for n in range(num):
            hand.append(self.remove(0))
        return hand

