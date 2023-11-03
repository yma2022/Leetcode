class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        curr = 0
        for i in range(1, max(target)+1):
            if target[curr] > i:
                res.append('Push')
                res.append('Pop')
            else:
                res.append('Push')
                curr += 1
        return res
        
        