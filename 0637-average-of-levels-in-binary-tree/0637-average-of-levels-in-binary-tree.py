# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        
        q = deque()
        res = []
        q.append(root)
        
        while q:
            total = 0
            k = len(q)
            for _ in range(len(q)):
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                    
                if curr.right:
                    q.append(curr.right)
                
            res.append(total/k)
            
        return res
        
        