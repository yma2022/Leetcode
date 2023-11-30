class Solution:
    def intToRoman(self, num: int) -> str:
        stack = []
        base = 1
        num = str(num)
        for i in range(len(num) - 1, -1, -1):
            if num[i] != 0:
                if num[i] == "4":
                    stack.append((5, base))
                    stack.append((1, base))
                elif num[i] == "9":
                    stack.append((1, base*10))
                    stack.append((1, base))
                else:
                    stack.append((int(num[i]), base))
            base *= 10
            
        d = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500: "D", 1000: "M"}
        
        ans =""
        
        while stack:
            ele = stack.pop()
            if ele[0] == 5 or ele[0] == 1:
                ans += d[ele[0] * ele[1]]
            else:
                k = ele[0]
                while k > 0:
                    if k > 5:
                        ans += d[5 * ele[1]]
                        k -= 5
                    else:
                        ans += d[ele[1]]
                        k -= 1
        return ans