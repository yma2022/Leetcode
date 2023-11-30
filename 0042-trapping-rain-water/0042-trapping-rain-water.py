class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid_h = stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                    d = min(height[i], height[stack[-1]]) - height[mid_h]
                    result += w * d
            stack.append(i)
        return result