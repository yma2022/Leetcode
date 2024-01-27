class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        books.append(-1)
        
        stk = []
        dp = [0] * (n + 1)
        
        for i in range(n):
            if books[i] > books[i - 1]:
                dp[i] = dp[i - 1] + books[i]
            else:
                _len = 0 # length of the consecutive ramp excluding [i]
                while True:
                    if not stk:
                        _len = min(i, books[i])
                        extra = 0
                        break
                    j = stk[-1]
                    upper_bound_j = books[i] - (i - j)
                    if books[j] >= upper_bound_j:
                        stk.pop()
                    else:
                        _len = (i - j - 1)
                        extra = dp[j]
                        break
                s = (books[i] + books[i] - _len) * (_len + 1) // 2
                dp[i] = s + extra
            stk.append(i)
        
        return max(dp)