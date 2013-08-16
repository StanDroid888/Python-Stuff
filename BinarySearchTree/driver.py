'''
Created on Aug 15, 2013

@author: Stanley Wong
'''
from treeNode import Node
from bst import BinarySearchTree

node3 = Node(3)

myTree = BinarySearchTree()

myTree.add(myTree.root,55)
myTree.add(myTree.root, 22)
myTree.add(myTree.root, 33)
myTree.add(myTree.root,11)
myTree.add(myTree.root, 44)
myTree.add(myTree.root, 88)

myTree.printInOrder(myTree.root)