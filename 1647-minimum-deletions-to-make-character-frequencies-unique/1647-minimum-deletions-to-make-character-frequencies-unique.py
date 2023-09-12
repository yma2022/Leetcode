class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(s)
        freq = []
        for key in d:
            freq.append(d[key])
        freq.sort()
        ans = 0
        #print(freq)
        for i in range(len(freq) - 2, -1, -1):
            for j in range(i + 1, len(freq)):                
                if freq[i] == freq[j]:
                    ans += 1 + freq[i] - freq[i + 1] if freq[i + 1] != 0 else freq[i]
                    freq[i] = freq[i + 1] - 1 if freq[i + 1] > 0 else 0
                    
        #print(freq)
        return ans
        