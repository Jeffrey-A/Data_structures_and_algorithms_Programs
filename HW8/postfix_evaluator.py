#Jeffrey Almanzar
from Stack import *

def postfix_eval(exp):
    '''Evaluates a postfix expresion.

    pre: exp is a valid postfix expresion.
    post: the result of the postfix expresion is printed out and the value is returned'''
    
    stack = Stack() #Stack
    try:
        for ch in exp:
            if ch not in '+-/*' and ch.isdigit(): # it's a number
                stack.push(ch) # push it to the stack

                
            elif ch in '+-*/': # it's an operation
                
                num_2 = int(stack.pop()) #Get the top number in the stack
                num_1 = int(stack.pop()) 
                
                if ch =='+':
                    stack.push(num_1 + num_2)
                elif ch =='-':
                    stack.push(num_1 - num_2)
                    
                elif ch =='*':
                    stack.push(num_1 * num_2)

                elif ch =='/':
                    stack.push(round(num_1/num_2,2))
                    
        print('  Valid postfix expresion!')
        return stack.items[0]
                
    except ValueError: #You passed an invalid character
        print("You did not pass a valid postfix expresion.")
        

    

               #Testing
print("Testing: 3*(4+5)-2+(3*6) = 3 4 5 + * 2 - 3 6 * + --> 43")
print('  Result:',postfix_eval('3 4 5 + * 2 - 3 6 * +'))
print()
print("Testing: (4-5)*2 = 4 5 - 2 * --> -2")
print('  Result:',postfix_eval('4 5 - 2 *'))
print()
print("Testing: (2+3)*4 = 23+4* --> 20")
print('  Result:',postfix_eval('23+4*'))
print()
print("Testing: (8/2)*4 = 82/4* --> 16")
print('  Result:',postfix_eval('82/4*'))

        
