class Solution:
    def isValid(self, s: str) -> bool:
        # init stack
        stack = list()
        # dict of brackets
        mapping = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            # if right bracket in mapping, check if the stack has left bracket
            if ch in mapping:
                top_element = stack.pop() if stack else ''
                
                if mapping[ch] != top_element:
                    return False
            # if it is left bracket, store in stack
            else:
                stack.append(ch)
        # return true if not stack    
        return not stack