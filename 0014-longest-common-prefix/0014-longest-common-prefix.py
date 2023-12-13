class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            if not prefix:
                return ""
            length = min(len(strs[i]), len(prefix))
            prefix = prefix[:length]
            for j in range(length):
                if prefix[j] == strs[i][j]:
                    continue
                else:
                    prefix = prefix[:j]
                    break
        return prefix