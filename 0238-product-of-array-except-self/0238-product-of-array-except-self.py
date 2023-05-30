class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [0] * n
        reverse = [0] * n
        res = []
        forward[0] = 1
        reverse[-1] = 1
        for i in range(1,n):
            forward[i] = forward[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            reverse[j] = reverse[j+1] * nums[j+1]
        for k in range(n):
            res.append(forward[k] * reverse[k])
            
        return res