class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            volume = (right - left) * min(height[left], height[right])
            maxVolume = max(volume, maxVolume)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxVolume