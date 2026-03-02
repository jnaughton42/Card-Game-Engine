# Card Game Engine (Spring 2026)
Programming in Python Assignment (In Progress)

## Description

Beginnings of a framework for card game logic, so far there are Deck and Card classes with basic functions
(insert, remove, deal, shuffle, showdeck). Hands will likely inherit from Deck class as they will have the 
same basic functionality. Currently very little code so not much to talk about

## Future Plans

- Abstract Deck class that can be inherited by game-specific deck classes and hand class
- Abstract player class that has a hand and has certain functions to interface with whatever resources/actions are available in a particular game
- Unit testing, exception handling, documentation all need to be added
- GUI layer for at least one game (maybe Texas Hold 'Em or Solitaire?)
- Multiple players?
