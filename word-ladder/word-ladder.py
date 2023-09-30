class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def findNeighbors(wordlist, word):
            nonlocal seen
            neighbors = []
            for w in wordlist:
                if len(w) != len(word) or w in seen:
                    continue
                diff = 0
                for c1, c2 in zip(word, w):
                    if c1 == c2:
                        continue
                    diff += 1
                if diff == 1:
                    seen.add(w)
                    neighbors.append(w)                
            return neighbors
        
        if endWord not in wordList:
            return 0
        
        q = deque()
        q.append((beginWord, 1))
        seen = set()
        while q:
            for _ in range(len(q)):
                word, dist = q.popleft()
                if word == endWord:
                    return dist
                neighbors = findNeighbors(wordList, word)
                # print(word, neighbors)
                for nei in neighbors:
                    q.append((nei, dist + 1))
        return 0
                
        
        
        