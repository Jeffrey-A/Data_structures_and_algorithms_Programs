#Jefrey Almanzar
class UI(object):
    """Prints info to the console"""

    def intro(self):
        """Prints an intro duction to the game"""
        print("####################################################")
        print("                 Welcome to The Game                ")
        print("   See the rules online, cheating is not tolerated  ")
        print("####################################################")
        print()

    def trump_suit(self,trump,cards):
        print("####################################################")
        print(" Trump suit: ",trump,"       Cards left: ",cards)
        print("####################################################")
        print()
        


    def current_player_card(self,card1,card2):
        """Print the current card of the player

        pre: card1 and card2 are objects of type Card
        post: print the the current card"""
        print("Player 1: ",card1)
        print("Player 2: ",card2)
        print()
          
    def won(self,winner=''):
        """Print who won the hand
        pre: winner is a string
        post: print who won the hand"""
        print("####################################################")
        print("             ",winner," ,you won the hand!!")
        print("####################################################")
        print()

    def tie(self):
        print("####################################################")
        print("                 HAND TIED!!")
        print("####################################################")
        print()

    def results(self,player1,player2):
        """Prints how many card each player have

        pre: player1 and player2 are two objects of type Player"""
        
        print("####################################################")
        print("                     Results                        ")
        print("####################################################")
        print()
              
        print("Player 1 your pile have ",player1.player_cards()," cards")
        print("Player 2 your pile have ",player2.player_cards()," cards")
        print()
        
        if player1.player_cards() == player2.player_cards():
            print("#########################################################")
            print("You tied, you have the same amount of cards in your piles")
            print("#########################################################")
            
        elif player1.player_cards() > player2.player_cards():
            print("####################################################")
            print("             Player 1 ,you won the game!!")
            print("####################################################")
            
        else:
            print("####################################################")
            print("             Player 2 ,you won the game!!")
            print("####################################################")
            
        
        

        
