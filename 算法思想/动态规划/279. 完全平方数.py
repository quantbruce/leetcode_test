279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

"""
执行用时：
5428 ms
, 在所有 Python3 提交中击败了
30.77%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

################方法1 动态规划

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]

#时间复杂度：O(N*N^0.5)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/perfect-squares/solution/dong-tai-gui-hua-bfs-zhu-xing-jie-shi-python3-by-2/



###############方法2 广度优先搜索遍历BFS

https://leetcode-cn.com/problems/perfect-squares/solution/dong-tai-gui-hua-bfs-zhu-xing-jie-shi-python3-by-2/



