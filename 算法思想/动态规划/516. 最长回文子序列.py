# 方法1 inspired by 小抄
"""
执行用时：
1964 ms
, 在所有 Python3 提交中击败了
17.39%
的用户
内存消耗：
31.8 MB
, 在所有 Python3 提交中击败了
15.46%
的用户
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

# 时间复杂度：O(N**2)
# 空间复杂度：O(N**2)
