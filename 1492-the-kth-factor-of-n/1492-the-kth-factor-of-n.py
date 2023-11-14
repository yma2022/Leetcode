class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n//2+2):
            if n % i == 0 and i not in factors:
                factors.append(i)
                if n//i not in factors:
                    factors.append(n//i)
        factors.sort()
        print(factors)
        return factors[k-1] if len(factors) >= k else -1
        