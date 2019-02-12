# Jeffrey Almanzar
#Exercise 3
""" Professor I created two version of selection sort, I timed them, and the selection_sort_2 runs faster, but I created it a little
bit different than the book specifies. Therefore, I created another version(selection_sort) which does exctly what excercises 3 states.
In addition, I created a function name 'test' that confirms it""" 


from time import time
import random 

def selection_sort(numbers):
    """This program sort a list of number in an increasing order.

    pre: numbers is a list of non-repeated integers containing 2 or more elements.
    post: it returns the list sorted from smallest to biggest."""
    
    n = len(numbers) #number of elements in the list                                                                      2 steps
    num_sorted = 0   #Index of sorted elements                                                                            1                                                               
    while num_sorted < n:                                                                                               # 2
        min_index = numbers.index(min(numbers[num_sorted:])) #Position of the smallest number in the list                 4
        numbers[num_sorted],numbers[min_index] = numbers[min_index], numbers[num_sorted] #smallest value swaps position with the no sorted value. 4
        num_sorted += 1       #2
    return numbers           #return the list sorted 1
    #  12n + 4  performance: Θ(n)

    
def selection_sort_2(numbers):
    """This program sort a list of integers in an increasing order.

    pre: numbers is a list of integers containing 2 or more elements.
    post: it returns the list sorted from smallest to biggest."""
    
    n = len(numbers) #number of elements in the list                                    2 steps
    num_sorted = 0   #numbers that have been sorted                                      1
    sorted_list = [] #sorted list                                                        1
    while num_sorted != n:                                                             #2
        m = min(numbers)      #Find the smallest element in the list                   2
        sorted_list.append(m) #place the smallest element in the sorted list           1
        numbers.remove(m)     # remove the smallest element from the given list        1
        num_sorted += 1       #indicate that one number was sorted                     2
    return sorted_list        #return the list sorted       1
    # 8n + 5   performance: Θ(n)

def test():
    """It just compares the two sorting programs above."""
    elements = random.sample(range(1,1001),1000)
        
    s = time()
    selection_sort(elements)
    e = time()
    took = e-s

    print("Selection_sort, sorting 1,000 elements --- time --> "+str(took))
    print()
    s = time()
    selection_sort_2(elements)
    e = time()
    took = e-s
    print("Selection_sort_2, sorting 1,000 elements --- time --> "+str(took))

test()


def running_time():
    """ It calculates the running time of the selection_sort funcion above.
    pre: none
    post: it prints the time spent. """

    ###################################
    # WARNING: IT WILL TAKE SOME TIME #
    ###################################
    list_1 = random.sample(range(1,10001),10000)    #create a random list of 10,000 elements
    list_2 = random.sample(range(1,100001),100000)  #create a random list of 100,000 elements
    list_3 = random.sample(range(1,1000001),1000000)#create a random list of 1,000,000 elements
    print("Random lists have been created:")

    #10,000
    start = time()
    selection_sort(list_1)
    end = time()
    time_spent = end - start
    print("Sorting 10,000 elements,the time was: "+ str(time_spent))
    print()

    #100,000
    start = time()
    selection_sort(list_2)
    end = time()
    time_spent = end - start
    print("Sorting 100,000 elements, the time was: "+ str(time_spent))
    print()


    #1,000,000
    start = time()
    selection_sort(list_3)
    end = time()
    time_spent = end - start
    print(" Sorting 10,000 elements, the time was: "+ str(time_spent))
    
              
    
    
    

    
