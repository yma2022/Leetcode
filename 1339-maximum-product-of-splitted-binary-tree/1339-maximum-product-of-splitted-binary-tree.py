# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            total_sum = left + right + root.val
            all_sums.append(total_sum)
            return total_sum
        
        total = dfs(root)
        ans = 0
        for s in all_sums:
            ans = max(ans, s * (total - s))
        
        return ans % (10**9 + 7)
        