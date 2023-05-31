class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b < b + a:
                return 1
            else:
                return -1
        if set(nums) == {0}:
            return "0"
        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp))
        return ''.join(nums_s)