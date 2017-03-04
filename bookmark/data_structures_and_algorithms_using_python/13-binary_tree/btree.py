# To implement a binary tree, we must explicitly store in each node the links to the two children along with the data
# stored in that node. We define the _BinTreeNode storage calss, for creating the nodes in a binary tree.
# Like other storage classes, the tree node class is meant for internal use only.
# 

# The storage class for creating binary tree nodes.
class _BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

## Tree Traversals
# A traversal iterates through a collection, one items at a time, in order to access or visit each item.
# The actual operation performed when "visiting an item is application dependent"

## Preorder traversal; Inorder traversal; Postorder traversal

## Preorder Traversal
# A tree traversal must begin with the root node, since that is the only access into the tree.
# After visiting the root node, we can then traverse the nodes in its left subtree followed by the nodes in its right subtree.
# Since every node is the root of its own subtree, we can repeat the same process on each node, resulting in a recursive solution.
# The base case occurs when a null child link is encountered since there will be no subtree to be processed from that link.
# The recursive operation can be viewed graphically.

## Given a binary tree of size n, a complete traversal of a binary tree visits each node once.
# If the visit operation only requires constant time, the tree traversal can be done in O(N)

class Solution:

    def preorderTrav(root):
        # base case
        if root is None:
            return
        print(root.data)
        # No necessary to judge whether left or right exist, as if they are None, it will return directly.
        self.preorderTrav(root.left)
        self.preorderTrav(root.right) 
     
    
