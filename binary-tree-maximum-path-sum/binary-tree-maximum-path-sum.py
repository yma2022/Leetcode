# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")
        
        def dfs(root):
            nonlocal max_path
            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            max_path = max(max_path, left + right + root.val)
            
            return max(left + root.val, right + root.val)
        
        dfs(root)
        
        return max_path
        