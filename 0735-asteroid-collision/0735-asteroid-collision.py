class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if not stack or stack[-1] / a > 0 or a > 0:
                stack.append(a)
            while stack and stack[-1] > 0 and a < 0:
                ele = stack.pop()
                if abs(ele) > abs(a):
                    stack.append(ele)
                    break
                elif abs(ele) == abs(a):
                    break
                else:
                    if not stack or stack[-1] / a > 0:
                        stack.append(a)
        return stack
                    
            
        