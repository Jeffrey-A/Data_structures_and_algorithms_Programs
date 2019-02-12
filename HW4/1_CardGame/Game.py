#Jeffrey Almanzar

from Player import Player
from Deck import Deck
from Card import Card
from UI import UI

class Game(object):
    """Top level class, it control the game."""

    def __init__(self):
        """Create the cards and shuffle them"""
        self.deck = Deck()
        self.player1 = Player(self.deck)#Create a player
        self.player2 = Player(self.deck)
        self.deck.shuffle()#creates the cards and shuffle them
        self.UI = UI()#will print info to the user
        

    def show_trumpsuit(self):
        """Shows the trump suit card.

        post: return the trump suit card. and shuffle the deck"""
        self.temp = self.deck.size()#cards left in the deck
        if self.temp >= 2: #There are more than 2 cards in the deck
            self.trumpsuit = self.deck.cards[0].suitName()#gets the top card's suit name of the shuffled deck
            self.deck.shuffle() #trumpsuit card is placed in a randow place
            self.UI.trump_suit(self.trumpsuit,self.temp) #Display the Trump suit
            return self.trumpsuit
            
        
    def select_card(self,player):
        """Select the top card from the deck and remove it.
        pre: player is an object of type Player
        post: the selected card is returned and remove from the deck"""
        return player.get_card()
    
    def hand(self):
        """Plays a complete hand.
        post: the selected cards will be remove from the deck and added to the pile of the winner player"""
        user = input("Player 1, hit enter to select your card-->")
        player1_card = self.select_card(self.player1)
        user = input("Player 2, hit enter to select your card-->")
        print()
        player2_card =self.select_card(self.player2)
        self.UI.current_player_card(player1_card,player2_card)

        if player1_card.suitName() == self.trumpsuit and player2_card.suitName()== self.trumpsuit: #Both player have the trumpsuit
            if player1_card > player2_card:  #player 1 card's rank is higher
                self.UI.won("Player 1")
                self.player1.add_card(player1_card) # add both card to his pile
                self.player1.add_card(player2_card)
                
            else:                             #player 2 card's rank is higher
                self.UI.won("Player 2")
                self.player2.add_card(player1_card)# add both card to his pile
                self.player2.add_card(player2_card)
                
        elif player1_card.suitName() == self.trumpsuit: #player 1 have the trumpsuit and player 2 do not
            self.UI.won("Player 1")
            self.player1.add_card(player1_card)
            self.player1.add_card(player2_card)

        elif player2_card.suitName() == self.trumpsuit: #player 2 have the trumpsuit and player 2 do not
            self.UI.won("Player 2")
            self.player2.add_card(player1_card)
            self.player2.add_card(player2_card)

        else:
            self.UI.tie() # Neither of the player got the trumpsuit

    def play_game(self):
        self.UI.intro() #print an introduction 
        
        while self.deck.size() >= 2: #If there are not card left, quit
            self.show_trumpsuit() #Show the trump card
            self.hand() # a whole hand is played
            user = input("Hit enter to play another round or type any letter to quit the game --> ")
            if user != '' : #The user wants to quit the game  
                break
        self.UI.results(self.player1,self.player2)


a = Game()
a.play_game()



        
        
