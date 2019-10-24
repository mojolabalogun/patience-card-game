from cards import InfiniteDeck
from threading import Timer

def confirm(response):
    return "y" in response.lower()

def init():
    print("\nWelcome to Patience | The Halting Problem Card Game!\n")
    print("Here's how to play!\n")
    print("Game Instructions:")
    print("Pick one card that exists in a standard deck (e.g. Ace of Spades, 2 of Clubs, etc)")
    print("Press 'Enter' to draw cards from an infinite deck.")
    print("If the card you chose eventually appears, you win!")
    print("Type anything and press 'Enter' to end the game.")
    print("If you end the game and your card wasn't in the deck, you win!")
    print("Good luck :) \n\n")
    playing  = input("Would you like to play? [type yes or no]: ")
    return playing

def main():
    playing = init()

    if confirm(playing):
        while True:
            print()
            rank = input("Choose a rank [1 - Ace, 2, 3, ..., 11 - Jack, 12 - Queen, 13 - King]: ")
            suit = input("Choose a suit [0 - Spades, 1 - Hearts, 2 - Clubs, 3 - Diamonds]: ")
            try:
                suit = int(suit)
                rank = int(rank)
                break
            except:
                print("Error: please enter a valid card!")
                continue
        
        deck = InfiniteDeck(suit, rank)
        print()
        print("You selected the %s!" % deck.card)
        print()
        while True:
            card = deck.next_card()
            if deck.in_deck and card == card:
                print("You win! The card you selected was in the deck!\n")
                break

            stop = input(str(card) + "\n")
            if stop == "":
                continue

            if not deck.in_deck:
                print("You win! The card you selected was not in the deck!\n")
            else:
                print("You lose! The card you selected was in the deck :(\n")
            break

    print("Play again next time!")
  
if __name__ == "__main__":
    main()