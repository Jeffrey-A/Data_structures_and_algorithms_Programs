#Jeffrey Almanzar

computed = 0 # Will help me to count how many times fib(3) is computed

def fib(n):
    """Recursive Fibonacci Program Modified.
    pre: n is an non negative integer.
    post: Calculates the nth number of the Fibonacci sequence, returns it, and also display tracing inf to the console.
          the global variable 'computed' is modify each time n= 3. """
    global computed
    
    if n ==0:
        return 0
    elif n == 1:
        return 1
    
    else:
        if n==3:# fib(3) is being computed
            computed += 1 
            
        #First part of the assigment 
        print("Computing fib({})".format(n))
        output = fib(n-1) + fib(n-2)
        print("Leaving fib({}) Returning {}".format(n,output))
        return output
   
    
#Testing
def test(n):
    print(fib(n))
    print("#########################################################")
    print("     fib(3) was computed {} times in the process.".format(computed))
    print("#########################################################")

#Second part of the assigment    
test(10)



    
    
