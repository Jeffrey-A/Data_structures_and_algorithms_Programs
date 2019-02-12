# LList.py
#Jeffrey Almanzar
from ListNode import ListNode

class LList:

    #------------------------------------------------------------

    def __init__(self, seq=()):

        """create an LList
        post: creates a list containing items in seq"""
     
        if seq == ():
            # No items to put in, create an empty list
            self.head = None
        else:
            # Create a node for the first item
            self.head = ListNode(seq[0], None)

            # Add remaining items keeping track of last node added
            self.last = self.head #Question 3 instance variable that refers to the last element of the LList
            for item in seq[1:]:
                self.last.link = ListNode(item, None)
                self.last = self.last.link

        self.size = len(seq)
   
    #------------------------------------------------------------

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    #------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''
        
        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

    #------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list
        post: x is appended onto the end of the list'''

        # create a new node containing x
        newNode = ListNode(x)

        # link it into the end of the list
        if self.head is not None:
            # non-empty list
            #node = self._find(self.size - 1)
            #node.link = newNode
            
            self.last.link = newNode
            self.last = newNode #Now the last item is the one appended
        else:
            # empty list
            # set self.head to new node
            self.head = newNode
        self.size += 1

    #------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item
    
    #------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

    #------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from 
        the list'''

        assert 0 <= position < self.size

        self._delete(position)

    #------------------------------------------------------------

    def _delete(self, position):

        #private method to delete item at location position from the list
        # pre: 0 <= position < self.size
        # post: the item at the specified position is removed from the list
        # and the item is returned (for use with pop)

        if position == 0:
            # save item from the initial node
            item = self.head.item

            # change self.head to point "over" the deleted node
            self.head = self.head.link

        elif position == self.size -1: #Deleting the last element, need to update the tail
            prev_node = self._find(position - 1)
            item = prev_node.link.item
            prev_node.link = None
            self.last = prev_node #update the tail
            

        else:
            # find the node immediately before the one to delete
            prev_node = self._find(position - 1)

            # save the item from node to delete
            item = prev_node.link.item

            # change predecessor to point "over" the deleted node
            prev_node.link = prev_node.link.link

        self.size -= 1
        return item

    #------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item

        pre: self.size > 0 and ((i is None or (0 <= i < self.size))

        post: if i is None, the last item in the list is removed
        and returned; otherwise the item at position i is removed 
        and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        # default is to delete last item
        # i could be zero so need to compare to None
        if i is None:
            i = self.size - 1
        
        return self._delete(i)

    #------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and 
              old elements from position i..oldsize-1 are at positions 
              i+1..newsize-1'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)
        else:
            # find item that node is to be insert after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)
        
        if i == self.size: #Now the last item is the one inserted
            self.last = self.last.link #update the tail
        self.size += 1

    #------------------------------------------------------------

    def __copy__(self):
    
        '''post: returns a new LList object that is a shallow copy of self'''
        
        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    #------------------------------------------------------------

    
##     def __iter__(self):

##         # generator version works in both Python2 and Python3
##         node = self.head
##         while node is not None:
##             yield node.item
##             node = node.link

    #------------------------------------------------------------

    def __iter__(self):

        return LListIterator(self.head)
    #------------------------------------------------------------
    
    #Question 1
    def __min__(self):
        """post: return the smallest item in the linked list."""
        startnode = self.head  #first node
        nextnode= self.head.link #second node
        minim = 0
        while nextnode is not None:
            if startnode.item < nextnode.item:
                minim = startnode.item #it's smaller
            else:
                minim = nextnode.item
                startnode = nextnode
            nextnode = nextnode.link
        return minim
        
    def __max__(self):
        """post: return the biggest item in the linked list."""
        startnode = self.head
        nextnode= self.head.link
        maxim = 0
        while nextnode is not None:
            if startnode.item > nextnode.item:
                maxim = startnode.item #it's bigger
            else:
                maxim = nextnode.item
                startnode = nextnode
            nextnode = nextnode.link
        return maxim
    
    def index(self,x):
        """pre: x is a item of type NodeList and another NodeList is likink to it
        post: return the position at which x is located."""
        pos = 0 # position of X
        node = self.head
        while node is not None:
            if node.item == x: #Position found
                return pos
            node = node.link
            pos+= 1
        
    def count(self,x):
        """pre: x is a item of type NodeList and another NodeList is likink to it
        post: return how many times x occurs in the linked list."""
        occu = 0 # number of occurances
        node = self.head
        while node is not None:
            if node.item == x:
                occu +=1
            node = node.link
        return occu
    
    def remove(self,x):
        """pre: x is a item of type NodeList and another NodeList is likink to it
        post: remove the element x from the linked list."""
        self._delete(self.index(x)) #find the position of x and then delete it

#------------------------------------------------------------

class LListIterator:

    #------------------------------------------------------------

    def __init__(self, head):
        self.currnode = head

    #------------------------------------------------------------
    # Python2 version
    def next(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

    #------------------------------------------------------------
    # Python3 version
    def __next__(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

def testing(seq=[]):
    """pre: seq is a sequence of 6 numbers. if seq > 6, the modify the insert statement below"""
    print('######################')
    print('# Testing: self.last #')
    print('######################')
    x = LList(seq)
    for i in x:
        print(i, end= ' ')
    print('\nLast item:',x.last.item)
    print()
    
    # After append
    print('Apending 7:')
    x.append(7)
    for i in x:
        print(i, end= ' ')
    print('\nLast item:',x.last.item)
    print()
    

    # After inser
    print("inserting 8 at the end")
    x.insert(7,8)
    for i in x:
        print(i, end=' ')
    print('\nLast item:',x.last.item)
    print()

    #After deleting the last element
    print('8 was deleted')
    x._delete(7)
    for i in x:
        print(i, end=' ')
    print('\nLast item:',x.last.item)
    print()

    #After poping out the last element
    print('7 was poped out')
    x.pop(6)
    for i in x:
        print(i, end=' ')
    print('\nLast item:',x.last.item)
    print()

    print('####################################')
    print('# Testing: the 5 new methods added #')
    print('####################################')
    
    #__min__ and __max__
    y = LList([23,75,2,80,100,75,15,6])
    for i in y:
        print(i, end=' ')
    print('\n Minimum -->',y.__min__(), '\n Maximum -->', y.__max__())

    #Index
    print(' index of 80 -->',y.index(80))

    #count
    print(' counting 75 -->',y.count(75),'times')

    #remove
    print()
    print('Removing 23, 2 and 6')
    y.remove(23)
    y.remove(2)
    y.remove(6)
    for i in y:
        print(i, end=' ')
                  
testing([1,2,3,4,5,6]) #Can test any other list, of the same lenght.
#For testing a list of diferent lenght, update the parameter in testing _delete and pop   
    
