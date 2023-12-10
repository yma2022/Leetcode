class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        q = deque()
        q.append((startGene, 0))
        
        def checkNeighbor(gene1: str, gene2: str) -> bool:
            score = 0
            for g1, g2 in zip(gene1, gene2):
                score += (g1!=g2)
            return score == 1
        visited = set()
        while q:
            node, step = q.popleft()
            if node == endGene:
                return step
            visited.add(node)
            for gene in bank:
                if checkNeighbor(gene, node) and gene not in visited:
                    q.append((gene, step+1))
        return -1
                        