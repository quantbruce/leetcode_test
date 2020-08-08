#############方法1 普通动态规划

"""
执行用时：
5676 ms     ##################这个时间复杂度太高了
, 在所有 Python3 提交中击败了
5.11%
的用户
内存消耗：
14.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0]*len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i]-min(prices[:i]))
        return dp[-1]
#时间复杂度：我觉得是O(N**2)？？？？？？？
#空间复杂度: O(N)

https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
    
    

################方法2 优化后的动态规划    
"""
执行用时 :
36 ms        #########################再看看这个时间，体会下优化的效率！！！！！！
, 在所有 Python3 提交中击败了
97.54%
的用户
内存消耗 :
14.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
#时间复杂度：O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
