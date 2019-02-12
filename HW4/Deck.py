# Deck.py
#Jeffrey Almanzar part 2
# def size() now is not needed, I am using an instance variable to get the size of the deck as suggested for exercise 1
import random
from Card import Card
  
class Deck(object):

    #------------------------------------------------------------

    def __init__(self):

        """post: Creates a 52 card deck in standard order"""

        cards = []
        self.deck_size = 0
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards
        self.deck_size = len(self.cards)
        
        #Questinon 1, self.deck_size is an instant variable which keeps track of the deck size.
        # It does not affect the running time efficiency of operations because both the original self.size()
        #and this instant variable are O(1) or theta(1), because of the len() function's efficiency is O(1) .
        
        


    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.deck_size > 0
        post: Returns the next card, and removes it from self.card if
        the deck is not empty, otherwise returns False"""
    
        if self.deck_size > 0:
            self.deck_size -= 1 #Update the size of the deck
            return self.cards.pop()
        else:
            return False

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck
        post: randomizes the order of cards in self"""
        #Question 2, from the random module, I am using the shuffle function
        random.shuffle(self.cards)

    #----------------------Question 3-----------------------------
    def addTop(self,card):  
        """pre: card is an instance of the class Card.
        post: adds a card to the deck and place it on the top"""
        self.cards.insert(0,card)
        self.deck_size += 1 #Update the size of the deck
        
                                            
    def addBottom(self,card): 
        """pre: card is an instance of the class Card.
        post: adds a card to deck and place it at the end of the deck"""
        self.cards.append(card) 
        self.deck_size += 1 #Update the size of the deck
        
                          
    def addRandom(self,card):
        """pre: self.deck_size > 0 and card is an instance of the class Card.
        post: adds a card to deck and place it on a random place"""
        if self.deck_size > 0: # The deck must contain some cards in it, in orther to insert a card in a random position
            i = random.randrange(0,self.deck_size) 
        else: # if there are not cards in the deck, insert it at the top
            i = 0
        self.cards.insert(i,card)
        self.deck_size += 1 #Update the size of the deck
        

    


def test():
    d = Deck()
    print("################--Testing size--################")
    print()
    
    print("Deck initial size --> ",d.deck_size)
    cards_dealt = []#Saves the cards dealt
    k = 0
    for i in range(10):  #Dealing ten cards to see if the size length changes
        cards_dealt.append(d.deal())
        k += 1
    print(k,'cards were dealt.')
    print(d.deck_size," cards left.")
    print()
    
    print("################--Testing shuffle--################")
    d.shuffle()
    print("The card must not be in ascending order after shuffling them:")
    print()
    for i in d.cards: #printing the cards to see if their original order change
        print(i, end ='--> ')
    print()
    print()
    print("################--Testing AddTop--################")
    d.addTop(cards_dealt.pop(0)) #adding this card to the top of the deck
    print('1 card was added.')
    print(d.deck_size," cards left.")
    print()
    
    
    print("################--Testing AddBottom--################")
    d.addBottom(cards_dealt.pop(0)) #adding this card to the end of the deck
    print('1 card was added.')
    print(d.deck_size," cards left.")
    print()

    
    print("################--Testing AddRandom--################")
    d.addRandom(cards_dealt.pop(0))#adding this card to a random place in the deck
    print('1 card was added.')
    print(d.deck_size," cards left.")
test()
       
