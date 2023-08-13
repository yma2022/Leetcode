# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.temp = []
        def dfs(node):
            if not node:
                return            
            
            dfs(node.left)
            self.temp.append(node)
            dfs(node.right)
            
        dfs(root)
        
        srt = sorted(n.val for n in self.temp)
        return srt[k - 1]