# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, sum):
        if not root:
            return 0
        count = 1 if root.val == sum else 0
        count += self.helper(root.left, sum - root.val)
        count += self.helper(root.right, sum - root.val)
        return count
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.helper(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) if root else 0
        