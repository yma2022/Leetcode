"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        new_root = Node(val=root.val)
        q = deque()
        q.append([root, new_root])
        
        while q:
            length = len(q)
            for _ in range(length):
                node, new_node = q.popleft()
                for child in node.children:
                    new_child = Node(val=child.val)
                    new_node.children.append(new_child)
                    q.append([child, new_child])
                    
        return new_root
            