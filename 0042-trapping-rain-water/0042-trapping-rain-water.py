class Solution:
    def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
        
#         n = len(height)
#         res = 0
#         left_max = [0 for _ in range(n)]
#         right_max = [0 for _ in range(n)]
#         left_max[0] = height[0]
        
#         for i in range(n):
#             left_max[i] = max(height[i], left_max[i-1])
        
#         right_max[-1] = height[-1]
#         for i in range(n-2, -1, -1):
#             right_max[i] = max(height[i], right_max[i + 1])
        
#         for i in range(n-1):
#             res += min(left_max[i], right_max[i]) - height[i]
            
#         return res
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid_height = stack.pop()
                if stack:
                    # 雨水高度是 min(凹槽左侧高度, 凹槽右侧高度) - 凹槽底部高度
                    h = min(height[stack[-1]], height[i]) - height[mid_height]
                    # 雨水宽度是 凹槽右侧的下标 - 凹槽左侧的下标 - 1
                    w = i - stack[-1] - 1
                    # 累计总雨水体积
                    result += h * w
            stack.append(i)
        return result
        
        