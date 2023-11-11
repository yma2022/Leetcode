class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_l_to_r = nums
        product_r_to_l = nums[::-1]
        
        for i in range(1, n):
            product_l_to_r[i] *= (product_l_to_r[i-1] or 1)
            product_r_to_l[i] *= (product_r_to_l[i-1] or 1)
            
        return max(max(product_l_to_r),max(product_r_to_l))
        