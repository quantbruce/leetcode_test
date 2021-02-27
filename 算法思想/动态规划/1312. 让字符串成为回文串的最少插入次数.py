# 方法1. inspired by 小抄

"""
执行用时：
832 ms
, 在所有 Python3 提交中击败了
27.34%
的用户
内存消耗：
17 MB
, 在所有 Python3 提交中击败了
15.23%
的用户
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][-1]
      
# 时间复杂度: O(N**2)
# 空间复杂度: O(N**2)

