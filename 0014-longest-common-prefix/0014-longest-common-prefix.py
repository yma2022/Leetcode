class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            if not prefix:
                return ""
            if len(strs[i]) < len(prefix):
                prefix = prefix[:len(strs[i])]
            for j in range(len(prefix)):
                if prefix[j] == strs[i][j]:
                    continue
                else:
                    prefix = prefix[:j]
                    break
        return prefix