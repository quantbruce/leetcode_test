https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian-shi-ti-10-ii-qing-wa-tiao-tai-jie-wen-ti-dong/

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
#时间复杂度：O(N)
#空间复杂度：O(1)

#########方法2 动态规划
##写的不太对...给别人检查下问题
class Solution:
    def numWays(self, n: int) -> int:
        dp = [1] * (n+2)
        dp[0] = 1
        dp[1] = 1
        while n >=2:
            dp[n] = dp[n-1] + dp[n-2]
        return dp[n]%1000000007

    
