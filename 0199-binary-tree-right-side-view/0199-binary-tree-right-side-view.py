# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None
        
        q = deque()
        res = []
        
        q.append(root)
        
        while q:
            idx = len(q) - 1
            for i in range(len(q)):                
                curr = q.popleft()
                if i == idx:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
        return res
                
            
        
        