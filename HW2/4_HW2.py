#Jeffrey almanzar HW-2

#Instruction:
"""4) Write a program that has both Linear Search and Binary Search algorithms implemented defined as two seprate functions.
Run each of the algorithms on the list of integers from 0 to 999999
and time them on three different numbers to search for: 10, 499999, and 999999.
At the end your program should print the results. """

#Using the skeleton of the program:

# This programs has implementation of two algorithms:
# linear search and binary search ...

from time import time

def linear_search(items,target):
  """ Searches for specific item in a list of items, looking at one item at a time.

     pre: items is a list of number and target is the number to search for.
     post: if the number is in the list, it returns its index, otherwise it returns -1."""
  
  i = 0
  while i < len(items):
      if items[i] == target: # number found, return its position(index)
          return i  
      i += 1
    
  return -1         # The number looking for, is not in the list 

 
def binary_search(items,target):
  """ Searches for specific item in a sorted list of items, cutting the list in half and comparing the middle item with the item looking for.

     pre: items is a sorted list of numbers and target is the number to search for.
     post: if the number is in the list, it returns its index otherwise it returns -1."""

  low = 0
  high = len(items)-1

  while low <= high:
      mid = (low + high)//2 # index of the middle value
      item = items[mid]
      if target == item:    # number found, return its position(index)
          return mid        
      elif target < item :  # search from the middle down 
          high = mid - 1    
      else:                  # search from the middle up
          low = mid + 1
    
  return -1               # The number looking for, is not in the list 


def main():

  numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999
  #print(numbers)

  #Linear search
  print("########################################################")
  print("#                 Linear Search                        #")
  print("########################################################")
  print()
  
  start = time()
  searching = linear_search(numbers,10)
  end = time()
  print("Searching 10, using linear search: ")
  print("Running time: " + str(end - start))
  print()
  
  start = time()
  searching = linear_search(numbers,499999)
  end = time()
  
  print("Searching 499999, using linear search: ")
  print("Running time: " + str(end - start))
  print()
  
  start = time()
  searching = linear_search(numbers,999999)
  end = time()

  print("Searching 999999, using linear search: ")
  print("Running time: " + str(end - start))
  print()
  
  #Binary search
  print("########################################################")
  print("#                 Binary Search                        #")
  print("########################################################")
  print()

  
  start = time()
  searching = binary_search(numbers,10)
  end = time()

  print("Searching 10, using binary search: ")
  print("Running time: " + str(end - start))
  print()
  
  start = time()
  searching = binary_search(numbers,499999)
  end = time()

  print("Searching 499999, using binary search: ")
  print("Running time: " + str(end - start))
  print()
  
  start = time()
  searching = binary_search(numbers,999999)
  end = time()

  print("Searching 999999, using binary search: ")
  print("Running time: " + str(end - start))
  print() 
  
main()
