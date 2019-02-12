#Jeffrey Almanzar

from BST import *
import unittest


class BST_test(unittest.TestCase):
    """Test BST methods: insert_rec(item) and find(item)."""
    
    def test_insert_rec(self):
        self.assertEqual(TREE.asList(),[2,3,5,7,8,9])
    def test_find(self):
        values_in = [8,2,9,5]
        for n in values_in:
            self.assertEqual(TREE.find(n),n) #assert that the value returned from find(n) ==n
            
        values_out = [11,1,4]
        for n in values_out:
            self.assertEqual(TREE.find(n),None)
        

TREE = BST()
TREE.insert_rec(7)
TREE.insert_rec(3)
TREE.insert_rec(8)
TREE.insert_rec(2)
TREE.insert_rec(5)
TREE.insert_rec(9)
  
if __name__ == '__main__':
  unittest.main()
