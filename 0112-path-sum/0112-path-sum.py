# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, node, sum):
        if not node.left and not node.right and sum == 0:
            return True
        if not node.left and not node.right:
            return False
        if node.left:
            sum -= node.left.val
            if self.traversal(node.left, sum):
                return True
            sum += node.left.val
        if node.right:
            sum -= node.right.val
            if self.traversal(node.right, sum):
                return True
            sum += node.right.val
            
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False           
        return self.traversal(root, targetSum - root.val)
        