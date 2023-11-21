class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def diff(num):
            # to get rev
            tmp = list(str(num))
            l, r = 0, len(tmp) - 1
            while l < r:
                tmp[l], tmp[r] = tmp[r], tmp[l]
                l += 1
                r -= 1
            rev = "".join(tmp)
            rev = int(rev)
            return rev - num
        hashmap = collections.defaultdict(int)
        for num in nums:
            hashmap[diff(num)] += 1
            
        ans = 0
        MOD = 10**9 + 7
        for key in hashmap:
            if hashmap[key] <= 1:
                continue
            ans += (hashmap[key] - 1) * hashmap[key] // 2
            ans %= MOD
                
        return ans
        