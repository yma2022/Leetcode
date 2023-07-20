# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        l_r_num=[0,0]
        def dfs(root):
            if root is None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                l_r_num[0],l_r_num[1]=left,right
            return left+right+1
        total = dfs(root)
        parent_num = n-sum(l_r_num)-1
        return max(parent_num,max(l_r_num))>n/2  