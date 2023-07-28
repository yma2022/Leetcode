class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        stack = [0]
        for j in range(1,len(nums)*2):
            # # 情况一情况二
            # if nums2[i]<=nums2[stack[-1]]:
            #     stack.append(i)
            # # 情况三
            # else:
            i = j % len(nums)
            while len(stack)!=0 and nums[i]>nums[stack[-1]]:               
                result[stack[-1]]=nums[i]
                stack.pop()                 
            stack.append(i)
        return result