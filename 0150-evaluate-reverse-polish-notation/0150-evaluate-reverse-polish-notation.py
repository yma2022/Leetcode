class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            st.append(t)
            # print(st)            
            if st[-1] in ["+", "-", "*", "/"]:
                ops = st.pop()
                num1 = int(st.pop())
                num2 = int(st.pop())
                # print(num1, num2)
                if ops == "+":
                    result = str(num1 + num2)
                elif ops == "-":
                    result = str(num2 - num1)
                elif ops == "*":
                    result = str(num2 * num1)
                elif ops == "/":
                    result = str(num2 // num1 + 1) if num2%num1 != 0 and num2//num1 < 0 else str(num2 // num1)
                st.append(result)
                
        return int(st[-1])
        