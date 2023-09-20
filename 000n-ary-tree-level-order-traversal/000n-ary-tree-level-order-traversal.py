"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        q = deque()
        res = []
        q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.children:
                    for i in range(len(curr.children)):
                        child = curr.children[i]
                        q.append(child)
            res.append(level)
            
        return res
                        
        