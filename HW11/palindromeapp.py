#Jeffrey Almanzar

#-------------------------------------------------------------------------------
#First part of the assignment
#-------------------------------------------------------------------------------
def rec_palindrome(phrase):
    '''Determines if a phrase is a palindrome.
    pre: phrase is string or list with no spaces and puntation in between.
    post: returns True if phrase is Palindrome, returns False otherwise'''
    if len(phrase)<=1: #base case:  if passing an empty string or just 1 letter return True
        return True  
    else: #recursive call: checks (first character == last character) and if it is true for the rest of the string
        first_last = phrase[0] == phrase[-1]
        return  first_last and rec_palindrome(phrase[1:-1])         
       

#-------------------------------------------------------------------------------
#Second part of the assignment
#-------------------------------------------------------------------------------
    
def remove(user):
    """Removes the spaces and puntuation in the string given.
    post: It calls rec_palindrome and prints the resualts.
    """
    
    if len(user) == 0: #Passing an empty string
        print("\t\t Not a palindrome!")
    elif len(user)> 0:
        phrase =[]
        for ch in user: #removing the spaces and puntuations of the given phrase
            if ch.isalpha():
                phrase.append(ch.lower())
        result = rec_palindrome(phrase) #Using rec_palindrome
        
    if result == True:
        print("\t\tIt is a PALINDROME!")
    else:
        print("\t\tNOT a palindrome!")
        
    
def palindromeApp():
    print("#########################################")
    print("     Welcome to the Palindrome App")
    print("You want to quit? hit enter or type --> q")
    print("#########################################")
    print()
    while True:
        user = input("\tType a phrase: ")
        if user == '' or user[0] =='q':
            print("Thank you")
            print("Exiting the program..")
            break
        remove(user)
#-------------------------------------------------------------------------------
# Testing and calling palindromeApp()
#-------------------------------------------------------------------------------

#Famous Palidrome Phrases
"""
Eva, Can I Stab Bats In A Cave?
A Man, A Plan, A Canal-Panama!
Mr. Owl Ate My Metal Worm
A Santa Lived As a Devil At NASA
"""

print("Testing rec_palindrome: ")
#Eva, Can I Stab Bats In A Cave? --True
print(rec_palindrome('evacanistabbatsinacave'))

#A Man, A Plan, A Canal-Panama! --True
print(rec_palindrome('amanaplanacanalpanama'))

#Hello world! -- False
print(rec_palindrome('helloworld'))
print()

palindromeApp()       
  
                
    
    

        
