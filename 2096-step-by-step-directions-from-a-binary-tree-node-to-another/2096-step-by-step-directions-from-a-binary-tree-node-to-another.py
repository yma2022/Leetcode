# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path, dest_path = [], []
        
        def dfs(root, path):
            nonlocal startValue, destValue, start_path, dest_path
            
            if root is None:
                return
            if root.val == startValue:
                start_path = path.copy()
            if root.val == destValue:
                dest_path = path.copy()
                
            path.append("L")
            dfs(root.left, path)
            path.pop()
            path.append("R")
            dfs(root.right, path)
            path.pop()
            
        dfs(root, [])
        
        start_path = "".join(start_path)
        dest_path = "".join(dest_path)
        
        i = 0
        while len(start_path) > i and len(dest_path) > i and start_path[i] == dest_path[i]:
            i += 1
        return (len(start_path) - i) * 'U' + dest_path[i:]

        