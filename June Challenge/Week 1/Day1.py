"""
Invert Binary Tree


Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if (root == None): 
            return None
        temp = root  
        self.invertTree(root.left)  
        self.invertTree(root.right)  
  
        temp = root.left  
        root.left = root.right  
        root.right = temp  
        return root
