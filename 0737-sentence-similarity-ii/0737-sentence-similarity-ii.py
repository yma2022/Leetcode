class Solution:
    def dfs(self, word1, word2, visited, similars):
        for similar in similars[word2]:
            if similar in visited: continue
            if word1 == similar:
                return True
            else:
                visited.add(similar)
                if self.dfs(word1, similar, visited, similars):
                    return True
        return False
    
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        similars = collections.defaultdict(set)
        for w1, w2 in similarPairs:
            similars[w1].add(w2)
            similars[w2].add(w1)
        print(similars)   
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and not self.dfs(w1, w2, set([w2]), similars):
                return False
        return True
        
        