class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        left, right = 0, len(height) - 1
        while left < right:
            volume = min(height[left], height[right]) * (right - left)
            maxVolume = max(maxVolume, volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxVolume