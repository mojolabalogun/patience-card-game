# Patience | The Halting Problem Card Game

## What is the Halting Problem?

"The halting problem is a decision problem in computability theory. It asks, given a computer program and an input, will the program terminate or will it run forever? [...] Halting problem is perhaps the most well-known problem that has been proven to be undecidable; that is, there is no program that can solve the halting problem for general enough computer programs. It's important to specify what kind of computer programs we're talking about. In the above case, it's a Python program, but in computation theory, people often use Turing machines which are proven to be as strong as "usual computers". In 1936, Alan Turing proved that the halting problem over Turing machines is undecidable using a Turing machine; that is, no Turing machine can decide correctly (terminate and produce the correct answer) for all possible program/input pairs." [Brilliant.com]

## The Objective

Patience is a single player card game that tests your patience. Players select a card and wait until it is revealed from an infinite deck
or end the game if they aren't convinced that their card exists in the deck. The game is a version of the halting problem but instead of asking "Does the program halt?", we ask, "Does your card exist in an infinite deck of cards?"

## Getting Started

Here is everything you need to play:

### Prerequisites

In order to run the game, you need to have python installed. Visit, https://realpython.com/installing-python/ for OS specific instructions.

### Running the Game

Navigate to the main directory and run the following:
```
python3 patience.py
```

### Game Instructions
* Pick one card that exists in a standard deck (e.g. Ace of Spades, 2 of Clubs)
* Now, just wait! Every second a card will be printed to the screen.
    * If your card eventually shows up you win!
    * Otherwise, you can press 'enter' at any point in the game to stop the
    game. If you stop the game, and your card is not in the deck you win!
* It's that simple :)

## Game Design

The game is essentially an infinite loop. The game uses two objects: a Card and an Infinite Deck. 
A Card has two attributes: suit and rank. And the Infinite Deck just has functions to generate the next
cards. It doesn't store generated cards due to the potential memory overhead for an infinite game.