class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, path, res):
            if len(path) > 1:
                res.append(path[:])
            uset = set()    
            for i in range(curr, len(nums)):
                if i > curr and nums[i] == nums[i-1]:
                    continue
                if path and nums[i] < path[-1] or nums[i] in uset:
                    continue
                uset.add(nums[i])
                path.append(nums[i])
                backtrack(i+1, path, res)
                path.pop()
                    
        results = []
        backtrack(0, [], results)
        return results
                
                
        