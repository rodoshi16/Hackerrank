"""

For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
The  value of every node is distinct.
For example, the image on the left below is a valid BST. The one on the right fails on several counts:
- All of the numbers on the right branch from the root are not larger than the root.
- All of the numbers on the right branch from node 5 are not larger than 5.
- All of the numbers on the left branch from node 5 are not smaller than 5.
- The data value 1 is repeated.

 

Given the root node of a binary tree, determine if it is a binary search tree.

Function Description

Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.

checkBST has the following parameter(s):

root: a reference to the root node of a tree to test
Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints

Output Format

Your function must return a boolean true if the tree is a binary search tree. Otherwise, it must return false.

Sample Input

image

Sample Output

Yes
Explanation

The tree in the diagram satisfies the ordering property for a Binary Search Tree, so we print Yes


"""
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode():
    temp =  node(-1)
    temp.left = None
    temp.right = None

    return(temp);
from math import inf
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    #checking if its a valid BST
    # low < root < high 
    
    def helper(root, low, high):
        if root is None:
            return True
        
        if not(low < root.data < high):
            return False
        
        return helper(root.left, low, root.data) and helper(root.right, root.data, high)
    
    return helper(root, -inf, inf)
            

ht = int(input())
cnt = 0
values = list(map(int, input().split(' ')))
root  = newNode()
def inorder(root, ht):
    global cnt
    global values
    if cnt == len(values):
        return
    else:
        if(ht>0):
            root.left = newNode();
            inorder(root.left, ht-1);
        root.data = values[cnt];
        cnt += 1
        if ht > 0:
            root.right = newNode();
            inorder(root.right, ht-1);
inorder(root, ht);
if(checkBST(root)):
    print("Yes")
else:
    print("No")