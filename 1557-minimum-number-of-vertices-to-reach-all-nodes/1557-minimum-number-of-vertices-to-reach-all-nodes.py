class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        isIncomingEdgeExists = [False for _ in range(n)]
        # print(isIncomingEdgeExists)
        for edge in edges:
            isIncomingEdgeExists[edge[1]] = True
            
        requiredNodes = []
        for i in range(n):
            if not isIncomingEdgeExists[i]:
                requiredNodes.append(i)
                
        return requiredNodes