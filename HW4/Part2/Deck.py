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
        # It does not affect the running time efficiency of operations because both the original self.size() and this instant variable
        # are O(1) or theta(1) (constant time, not depending of actual length of the element), because of then len() function.
        


    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card, and removes it from self.card if
        the deck is not empty, otherwise returns False"""
        self.deck_size = len(self.cards)-1

        if self.deck_size > 0:
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
    def addTop(self,rank,suit):
        """pre: rank is an positive integer > 1, suit is a string 'c','d','h' or 's'.
        post: adds a card to the deck and place it on the top"""
        self.cards.insert(0,Card(rank,suit))
        
                                            
    def addBottom(self,rank,suit):
        """pre: rank is an positive integer >1, suit is a string 'c','d','h' or 's'.
        post: adds a card to deck and place it at the end of the deck"""
        self.cards.insert(self.deck_size-1,Card(rank,suit))
        
                          
    def addRandom(self,rank,suit):
        """pre: rank is an positive integer >1, suit is a string 'c','d','h' or 's'.
        post: adds a card to deck and place it on a random place"""
        if self.deck_size > 0: # The deck must contain some cards in it, in orther to insert a card in a random position
            i = random.randrange(0,self.deck_size-2)# for testing purposes, I do not want this card to be placed at the end
        else: #insert the card at the top
            i = 0
        self.cards.insert(i,Card(rank,suit))
        self.deck_size = len(self.cards)
        

    


def test():
    d = Deck()
    print("################Testing size################")
    print()
    
    print("Deck initial size --> ",d.deck_size)
    for i in range(10):  #Dealing ten cards to see if the size length changes
        print("Card dealt!--> ",d.deal())
        print(d.deck_size," cards left.")
    print()
    
    print("################Testing shuffle################")
    d.shuffle()
    print("The card must not be in ascending order after shuffling them")
    for i in d.cards: #printing the cards to see if their original order change
        print(i)
    print()
    
    print("################Testing AddTop################")
    d.addTop(10,'s')
    print("d.addTop(10,'s')",d.cards[0])
    print()

    
    print("################Testing AddBottom################")
    d.addBottom(6,'c')
    print("d.addBottom(6,'c')",d.cards[d.deck_size-1])
    print()

    
    print("################Testing AddRandom################")
    d.addRandom(14,'h')
    print("After d.addRandom(14,'h')  the size is: ",d.deck_size) #must be equal to 45
    print("10 cards were dealt and 3 cards were added")#For this reason
test()
       
