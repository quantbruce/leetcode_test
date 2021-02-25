### 方法一：inspired by 算法小抄

"""
执行用时：
92 ms
, 在所有 Python3 提交中击败了
97.62%
的用户
内存消耗：
17.3 MB
, 在所有 Python3 提交中击败了
72.01%
的用户
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)] 
            if i == -1: return j + 1
            if j == -1: return i + 1
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,
                    dp(i - 1, j) + 1,
                    dp(i-1, j-1) + 1
                )
            return memo[(i, j)]
        return dp(len(word1)-1, len(word2)-1)
        
# 时间复杂度：O(min(M, N))
# 空间复杂度：O(M+N)


