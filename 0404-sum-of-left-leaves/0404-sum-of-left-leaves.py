# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def process(subtree, is_left):
            if not subtree.left and not subtree.right:
                return subtree.val if is_left else 0
            
            total = 0
            if subtree.left:
                total += process(subtree.left, True)
            if subtree.right:
                total += process(subtree.right, False)
            return total
        return process(root, False)
        