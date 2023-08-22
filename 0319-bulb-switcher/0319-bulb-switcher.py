class Solution:
    def bulbSwitch(self, n: int) -> int:
#         bulbs = [0 for _ in range(n)]
#         curr = 1
#         while curr <= n:
#             for i in range(n):
#                 if (i + 1) % curr == 0:
#                     bulbs[i] = (bulbs[i] + 1) % 2
#             curr += 1
                
#         return sum(bulbs)
        return int(sqrt(n))
            
        