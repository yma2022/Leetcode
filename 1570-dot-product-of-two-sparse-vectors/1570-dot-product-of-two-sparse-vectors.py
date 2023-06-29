class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i in range(len(nums)):
            if nums[i]:
                self.vector[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for key, val in self.vector.items():
            if key in vec.vector:
                product += val * vec.vector[key]
        return product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)