class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = dict()
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        res = 0
        for key in freq:
            if freq[key] == 1:
                return -1
            elif freq[key] %3 == 0:
                res += freq[key] // 3
            else:
                res += freq[key] // 3 + 1
        return res
        
                
                
        