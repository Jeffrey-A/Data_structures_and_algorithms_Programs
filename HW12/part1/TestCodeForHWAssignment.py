#Jeffrey Almanzar
from BST import BST

def main():
    # testing recursive find, pre- and post-order, and __len__

    """ creating the following BST:
                           25
                  15                29
            12         20      27        50
                    17 """
    t1 = BST()
    t1.insert_rec(25)
    t1.insert_rec(15)
    t1.insert_rec(12)
    t1.insert_rec(20)
    t1.insert_rec(17)
    t1.insert_rec(29)
    t1.insert_rec(27)
    t1.insert_rec(50)    

    
     
    print("The preorder traversal of the tree:", list(t1.preOrder_gen()))
##
##    print("The postorder traversal of the tree:", list(t1.postOrder_gen()))
    
    print("The length of the BST tree is ",t1.__len__())
    print("Let's see if we can find 27 using the non-recursive find: ", t1.find(27))
    print("Let's see if we can find 27 using the recursive find: ", t1.rec_find(27))


main()
