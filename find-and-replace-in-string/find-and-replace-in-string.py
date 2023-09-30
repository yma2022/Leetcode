class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        curr = 0
        res = ""
        d = collections.defaultdict(list)        
        for idx, src, target in zip(indices, sources, targets):
            d[idx].append((src, target))
        
        for i in range(len(s)):
            if i in d:
                if i > curr:
                    res += s[curr:i]
                curr = i
                for src, target in d[i]:
                    if s[i:i + len(src)] != src:
                        continue
                    res += target
                    curr = i + len(src)

        if curr != len(s):
            res += s[curr:]
        return res
        