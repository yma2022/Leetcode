class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                st.append(int(t))
            else:
                # print(st)
                num1 = st.pop()
                num2 = st.pop()
                if t == "+":
                    newNum = num1 + num2
                elif t == "-":
                    newNum = num2 - num1
                elif t == "*":
                    newNum = num2 * num1
                else:
                    newNum = abs(num2)//abs(num1)
                    newNum = -newNum if num2*num1 < 0 else newNum
                st.append(newNum)
                
        return st[-1]
                    