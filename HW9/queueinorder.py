#Jeffrey Almanzar
from MyQueue import Queue
import copy

def queueInOrder(someQueue):
    """pre: someQueue is a Queue.
    post: returns True if someQueue is in sorted order, returns False otherwise."""
    if isAcending(someQueue) == True or isDecending(someQueue) ==True:
        return True
    else:
        return False
    

# isAcending and isDecending are helper functions

def isAcending(someQueue):
    """pre: someQueue is a Queue.
    post: returns True if someQueue is in ascending order, returns False otherwise."""
    queue_1 = copy.deepcopy(someQueue)
    queue_2 = copy.deepcopy(someQueue)
    queue_2.dequeue()
    
    while queue_2.size() >0:
        first = queue_1.dequeue()
        nextI = queue_2.dequeue()
        if first > nextI: #If the first element is > than the second element, 
            return False                    #then it is not in ascending order 
    return True

def isDecending(someQueue):
    """pre: someQueue is a Queue.
    post: returns True if someQueue is in descending order, returns False otherwise."""
    queue_1 = copy.deepcopy(someQueue)
    queue_2 = copy.deepcopy(someQueue)
    queue_2.dequeue()
    
    while queue_2.size() >0:
        first = queue_1.dequeue()
        nextI = queue_2.dequeue()
        if first < nextI: #If the first element is < than the second element, 
            return False                    #then it is not in ascending order 
    return True

    
    






#Testing
#In ascending order
#------------------------------------------------------------------
x = Queue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)
x.enqueue(6)
print("Queue:",x.q)
print("In sorted order --> ",queueInOrder(x))
print("After the function call -->  Queue:",x.q)
print()

#In descending order
#------------------------------------------------------------------
x = Queue()
x.enqueue(5)
x.enqueue(4)
x.enqueue(3)
x.enqueue(2)
x.enqueue(1)
print("Queue:",x.q)
print("In sorted order --> ",queueInOrder(x))
print("After the function call -->  Queue:",x.q)
print()

#Not in order
#------------------------------------------------------------------
x = Queue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(5)
x.enqueue(4)
print("Queue:",x.q)
print("In sorted order --> ",queueInOrder(x))
print("After the function call -->  Queue:",x.q)
print()

#Not in order
#------------------------------------------------------------------
x = Queue()
x.enqueue(2)
x.enqueue(1)
x.enqueue(4)
x.enqueue(5)
x.enqueue(3)
print("Queue:",x.q)
print("In sorted order --> ",queueInOrder(x))
print("After the function call -->  Queue:",x.q)
print()
            
            




