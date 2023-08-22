class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            d[key].append(s)
        for key in d:
            res.append(d[key])
        return res
                
        