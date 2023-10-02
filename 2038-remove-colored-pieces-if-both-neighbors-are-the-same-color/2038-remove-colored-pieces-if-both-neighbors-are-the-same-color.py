class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        diff = 0
        curr = None
        length = 0
        i = 0
        while i < len(colors):
            # print(curr, length)
            if colors[i] == curr:
                length += 1
            if colors[i] != curr or i == len(colors) - 1:
                if length >= 3:
                    if curr == "A":
                        diff += length - 2
                    else:
                        diff -= length - 2
                curr = colors[i]
                length = 1
            i += 1
        return diff > 0
            
        