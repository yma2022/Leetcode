# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root):
            if not root:
                return -1
            depth = max(dfs(root.left), dfs(root.right))+1
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            return depth
        res = []
        dfs(root)
        return res