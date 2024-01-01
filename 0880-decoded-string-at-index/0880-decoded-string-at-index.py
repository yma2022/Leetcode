class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i, c in enumerate(s):
            size = size*int(c) if c.isdigit() else size + 1
            if k <= size:
                break
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                size /= int(c)
                k %= size
            else:
                if k == 0 or k == size:
                    return c
                size -= 1