# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        g, kids, parents = defaultdict(list), set(), set()
        for parent, kid, left in descriptions:
            kids.add(kid)
            parents.add(parent)
            g[parent].append([kid, left])
        parents.difference_update(kids)
        root = TreeNode(parents.pop())
        dq = deque([root])
        while dq:
            parent = dq.popleft()
            for kid, left in g.pop(parent.val, []):
                kid_node = TreeNode(kid)                
                if left == 1:
                    parent.left = kid_node
                else:
                    parent.right = kid_node
                dq.append(kid_node)
        return root