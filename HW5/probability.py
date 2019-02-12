from Solitaire import *

def probabilty(S,N):
    """Finds probability of winning.
    pre: S is the number of Simulation and N is the number of cards to be dealt.
    post: prints the probability of winning."""
    wins = 0 #Number of wins
    for i in range(S):  #Will play S games on N cards
        g = SolitaireGame(N)
        g.newGame()
        result = g.playGame()
        if result == True:
            wins += 1 #Player won 
        
    probabilty =  round((wins/S)*100,1)
    
    print("Probability of winning in {} games on {} cards : wins:{} --> {}% of probability winning".format(S,N,wins,probabilty))

print("###########################################################")
print("#                 Calculating Probability                 #")
print("###########################################################")
print()
probabilty(50,5)
print("###########################################################")
print("#                 Calculating Probability                 #")
print("###########################################################")
print()
probabilty(15,10)
print("###########################################################")
print("#                 Calculating Probability                 #")
print("###########################################################")
print()
probabilty(30,10)
