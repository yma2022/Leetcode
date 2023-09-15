# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        leafs = self.bfs(root)
        return self.LCA(root, leafs)
        
    def bfs(self, node):
        q = [node]
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)
            if not q:
                return level #return a list
        
        
    def LCA(self, root, nodes): #nodes going to be list of deepest nodes
        if not root:
            return None
        
        if root in nodes:
            return root
        
        left = self.LCA(root.left, nodes)
        right = self.LCA(root.right, nodes)
        
        if left and right:
            return root
        
        else:
            return left or right
        