class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        d = collections.defaultdict(list)
        curr = colors[0]
        length = 0
        i = 0
        while i < len(colors):
            # print(curr, length)
            if colors[i] == curr:
                length += 1
            if colors[i] != curr or i == len(colors) - 1:
                if length >= 3:
                    d[curr].append(length)
                curr = colors[i]
                length = 1
            i += 1
        opA = sum(d["A"]) - 2 * len(d["A"])
        opB = sum(d["B"]) - 2 * len(d["B"])
        return opA > opB
            
        