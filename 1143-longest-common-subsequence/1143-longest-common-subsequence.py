class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, len(text1)):
            dp[i][0] = min(1, dp[i-1][0] + 1) if text1[i] == text2[0] else dp[i-1][0]
            
        for j in range(len(text2)):
            dp[0][j] = min(1, dp[0][j-1] + 1) if text1[0] == text2[j] else dp[0][j-1]
            
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)            
        return dp[-1][-1]
        