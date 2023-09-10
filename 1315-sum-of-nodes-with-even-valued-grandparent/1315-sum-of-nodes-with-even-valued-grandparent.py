# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def calcSum(root, parent, gparent):
            if not root:
                return 0
            return calcSum(root.left, root.val, parent) + calcSum(root.right, root.val, parent) + (root.val if gparent % 2 == 0 else 0)
        
        return calcSum(root, -1, -1)
        
        