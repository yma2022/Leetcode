# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        leaves = self.bfs(root)
        return self.LCA(root, leaves)        
       
    def bfs(self, root):
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)
            if not q:
                return level
        
        
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