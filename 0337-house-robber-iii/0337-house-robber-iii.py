# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        lookup = {}
        def dfs(root):
            if not root: return 0
            if root in lookup: return lookup[root]
            val = 0
            if root.left:
                val+=dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                val+=dfs(root.right.left) + dfs(root.right.right)
            val=max(val+root.val, dfs(root.left)+dfs(root.right))
            lookup[root]=val
            return val
        return dfs(root)
            
                
            
        