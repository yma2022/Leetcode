"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        pseudoHead = Node(0,None,head,None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next