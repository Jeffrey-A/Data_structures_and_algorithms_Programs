#Jeffrey almanzar
#Exercise 9

def squeeze(items):
    """It takes out the duplicates of a sorted list.

    pre: items is a sorted list of numbers.
    post: it returns the sorted list with no repetion of elements."""
    new_list = []                      #1step 
    for i in items:                    # n
        if i not in new_list:          # 1
            new_list.append(i)
    return new_list                 #1
        
# T(n) = 2n + 2    performance: Θ(n)
    
