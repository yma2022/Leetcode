class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        d = collections.defaultdict(int)
        curr = colors[0]
        length = 0
        i = 0
        while i < len(colors):
            # print(curr, length)
            if colors[i] == curr:
                length += 1
            if colors[i] != curr or i == len(colors) - 1:
                if length >= 3:
                    d[curr] += length - 2
                curr = colors[i]
                length = 1
            i += 1
        return d["A"] > d["B"]
            
        