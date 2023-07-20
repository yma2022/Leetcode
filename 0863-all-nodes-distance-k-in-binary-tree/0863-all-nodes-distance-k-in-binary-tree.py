# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        def dfs(parent, child):
            if not child:
                return
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val] .append(parent.val)
                
            dfs(child, child.left)
            dfs(child, child.right)
            return
            
        dfs(None, root)
        
        queue = deque([target.val])
        visited = set()
        visited.add(target.val)
        while k:
            for i in range(len(queue)):
                parent = queue.popleft()
                visited.add(parent)
                for child in graph[parent]:
                    if child not in visited:
                        queue.append(child)
            k -= 1
        return list(queue)