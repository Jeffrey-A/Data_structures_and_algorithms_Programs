#Jeffrey almanzar

from Deck import Deck



class Player(object):
    """"Contains all the action that a player can make
    and keep track of the number of cards the player have in the pile."""
    
    def __init__(self,deck):
        """pre: deck is an object of type Deck"""
        self.player_pile = []
        self.d = deck

    def get_card(self):
        """Get the top card in the deck
        post: return the the top card of the deck"""
        self.temp= self.d.deal() #temporal card dealt to the player
        return self.temp
        

    def add_card(self,card):
        """it adds a card to the player's pile
        pre: card is a tupple (rank,suit)
        post: none"""
        self.player_pile.append(card)#add a card to the player's pile
        
    def player_cards(self):
        """post: returns the amount of card in the player's pile"""
        return len(self.player_pile)


    
   
    
    
               
        
        
        
