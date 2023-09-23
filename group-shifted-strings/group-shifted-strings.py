class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for w in strings:
            key = list(w)
            diff = ord(key[0]) - ord('a')
            for i in range(len(key)):
                key[i] = chr((ord(key[i]) - diff) % 26)
            key = "".join(key)
            d[key].append(w)
        # print(d)
        res = []
        for k in d:
            res.append(d[k])
        return res
        