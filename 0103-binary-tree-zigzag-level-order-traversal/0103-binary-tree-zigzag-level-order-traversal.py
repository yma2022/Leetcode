# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            length = len(q)
            level = []
            for i in range(length):
                node, idx = q.popleft()
                if idx%2 == 0:
                    level.append(node.val)
                else:
                    level = [node.val] + level
                
                if node.left:
                    q.append((node.left, idx+1))
                if node.right:
                    q.append((node.right, idx+1))
                    
            res.append(level)
            
        return res
        