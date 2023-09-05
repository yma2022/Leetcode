class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        for i in range(len(s)):
            if s[i] == "]":
                decoded = ""
                while stack[-1] != "[":
                    decoded += stack[-1]
                    stack.pop()
                stack.pop()
                
                base = 1
                k = 0
                
                while stack and stack[-1].isdigit():
                    k = k + int(stack[-1]) * base
                    stack.pop()
                    base *= 10
                
                currentLen = len(decoded)
                while k != 0:
                    for j in range(len(decoded) - 1, -1, -1):
                        stack.append(decoded[j])
                    k -= 1
            else:
                stack.append(s[i])
                
        for i in range(len(stack) - 1, -1, -1):
            ans = stack[-1] + ans
            stack.pop()
        return ans
        