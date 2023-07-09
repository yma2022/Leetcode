# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            
            elif is_identical(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        def is_identical(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2
            
            return (node1.val == node2.val) and is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)
        
        return dfs(root)
        
        