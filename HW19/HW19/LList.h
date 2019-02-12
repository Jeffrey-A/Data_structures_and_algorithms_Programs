// LList.h
#ifndef _LLIST_H
#define _LLIST_H

#include "ListNode.h"

class LList {

public:
  LList(); // sonstructor
  LList(const LList& source); // copy constructor
  ~LList();  // destructor

  LList& operator=(const LList& source); // assignment operator
  int size() { return size_; }  // size method
  void append(ItemType x);  // append operator
  void insert(size_t i, ItemType x); // insertion operator
  ItemType pop(int i=-1); // pop method
  ItemType& operator[](size_t position); // myLlist[position] for both assignment and access 
  
private:
  // methods
  void copy(const LList &source); // helper method for copy constructor
  void dealloc(); // helper method for destructor
  ListNode* _find(size_t position); // find method
  ItemType _delete(size_t position); // delete item from a linked list method
  
  // data elements
  ListNode *head_; // link to the nead node
  int size_; // info about linked list size
};

#endif // _LLIST_H
