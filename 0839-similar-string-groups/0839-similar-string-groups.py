class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        res = 0
        n = len(strs)
        
        root = []
        for i in range(n):
            root.append(i)
        for i in range(n):
            for j in range(i):
                if not self.isSimilar(strs[i], strs[j]):
                    continue
                root[self.getRoot(root, j)] = i
        for i in range(n):
            if root[i] == i:
                res += 1
        return res
    
    def getRoot(self, root, i):
        return i if root[i] == i else self.getRoot(root, root[i])
    
    def isSimilar(self, str1, str2):
        cnt = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                continue
            cnt += 1
            if  cnt > 2:
                return False
        return True