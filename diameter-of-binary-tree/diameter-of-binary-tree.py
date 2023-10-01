# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal diameter
            if not node:
                return 0
            left, right = helper(node.left), helper(node.right)
            diameter = max(left + right, diameter)
            return max(left, right) + 1
        diameter = 0
        helper(root)
        return diameter
        