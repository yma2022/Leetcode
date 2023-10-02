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
                d[curr].append(length)
                curr = colors[i]
                length = 1
            i += 1
        opA, opB = 0, 0
        for l in d["A"]:
            if l >= 3:
                opA += l - 2
        for k in d["B"]:
            if k >= 3:
                opB += k - 2
        # print(d)
        return opA > opB
            
        