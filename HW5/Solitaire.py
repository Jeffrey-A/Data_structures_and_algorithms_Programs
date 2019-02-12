from Card import *
from Deck import *
import itertools  # an interesting module that I found that contaings many useful functions for iteration

class SolitaireGame(object):
    """ a simple Solitaire Game: N cards are dealt face up on the table.
    If two cards have a matching rank, new cards are dealt face up on top of them.
    Dealing continues until the deck is empty, or no two stacks have matching ranks.
    The player wins if all the cards are dealt."""

    def __init__(self,N):
        """Constructor
        pre: N is an integer, denotes the number of piles, s.t. 1 < N < 50
        post: self.size is the number of piles"""

        if N < 1 or N>50:
            raise ValueError
        self.size = N

    def newGame(self):
        """ Creates a new game
        post: creates an instance of Solitaire game with N empty places"""
        
        self.deck = Deck() # creating a deck of cards
        self.deck.shuffle() # shuffling them in place

        self.cards_dealt = []
        for i in range(self.size):   # Deals self.size(N) cards
            self.cards_dealt.append(self.deck.deal())

    def playRound(self):
        """ a round of a game
        pre: all piles are not empty
        post: piles with same rank get new cards on top of them,
        returns True if successful, and False if no cards were placed into piles"""
    
        
        self.repeated_cards= False
        if len(self.deck.cards) > 0: #There are cards in the deck
            
            try:
                for i,j in itertools.combinations(self.cards_dealt, 2): #Comparing the cards i and j
                    if i.rankName() == j.rankName(): # Maching rank
                        #Getting position of the cards
                        pos1 =  self.cards_dealt.index(i)
                        pos2 =  self.cards_dealt.index(j)
        
                        
                        #Replacing cards
                        if len(self.deck.cards) > 0:
                            self.cards_dealt[pos1] = self.deck.deal()
                        if len(self.deck.cards) > 0:
                            self.cards_dealt[pos2]= self.deck.deal()
                        
                        self.repeated_cards = True #Indicates cards where replaced
                        
            except ValueError:
                return True #More than two cards matching rank, the program only handle two
            
            except AttributeError:
                return False #DECK EMPTY!, player won, not cards were replaced
            

            if self.repeated_cards == True: #Cards placed in the pile
                return True
        else:
            return False  #No cards placed in the pile
            
        
        

    def playGame(self):
        """ plays a Solitaire game
        post: returns True, if player wins, and False otherwise"""
        
        
        roundResult = True # initially, to enter the while loop's body
            
        while roundResult:
            roundResult = self.playRound()

        if roundResult== False : # all cards were dealt from the deck, success!
            return True
        else: # not all cards were dealt from the deck, the player lost
            return False

        

        
            
class test_solitaire(object):
    """Testing the solitaire game"""
    
    def __init__(self,N):
        """Creates an instance of the SolitaireGame.
        pre: N is an integer indicationg the number of cards to be dealt.
        post: creates a pile on N cards"""

        self.s = SolitaireGame(N)
        self.s.newGame()
        self.size = N

    def intro(self):
        print("###########################################################")
        print("#        TESTING THE SOLITAIRE GAME  on {} cards          #".format(self.size))
        print("###########################################################")
        print()
        
    def p_cards(self):
        """Display the current cards."""
        
        print("PILE OF CARDS:")
        k = 1
        for i in self.s.cards_dealt:
            print('   ',str(k)+'-',i)
            k += 1
        cards = len(self.s.deck.cards) #cards left in the deck
            
        print('Cards in the deck:',cards)
        
    def t_playGame(self):
        """Testing the playRound method"""
        r = self.s.playGame()
        if r == True:
            result = "Player won."
        else:
            result = "Player lost."
        print("#---------------------------------------------------------#")
        print("#                        Game Played                      #")
        print("#---------------------------------------------------------#")
        print(result)
   

#Tests on 5 cards
ts= test_solitaire(5)
ts.intro()
print("STARTING CARDS:")
ts.p_cards()
ts.t_playGame()
ts.p_cards()

#Tests on 10 cards
ts= test_solitaire(10)
ts.intro()
print("---STARTING CARDS----")
ts.p_cards()
ts.t_playGame()
ts.p_cards()

#Tests on 15 cards
ts= test_solitaire(15)
ts.intro()
print("---STARTING CARDS----")
ts.p_cards()
ts.t_playGame()
ts.p_cards()




     


                    
        
                    
        
            
        

        
        
    
