"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.visited = {}
        def getClonedNode(node):
            # If node exists then
            if node:
                # Check if its in the visited dictionary          
                if node in self.visited:
                    # If its in the visited dictionary then return the new node reference from the dictionary
                    return self.visited[node]
                else:
                    # Otherwise create a new node, save the reference in the visited dictionary and return it.
                    self.visited[node] = Node(node.val, None, None)
                    return self.visited[node]
            return None
        if not head:
            return head

        old_node = head
        # Creating the new head node.       
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = getClonedNode(old_node.random)
            new_node.next = getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]
        