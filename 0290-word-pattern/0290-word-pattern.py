class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = [''] * 26
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            key = ord(pattern[i]) - ord('a')
            if d[key] and d[key] == words[i]:
                continue
            if d[key] and d[key] != words[i]:
                return False
            else:
                if words[i] in d:
                    return False
                else:
                    d[key] = words[i]
        return True