121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


###########方法1 暴力遍历法

"""
超时
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                ans = max(ans, prices[j]-prices[i])     
        return ans
        
###########方法2 一次遍历法 (最优)

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
88.33%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
5.00%
的用户
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price-min_price, max_profit)
        return max_profit

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/


###############方法3 动态规划

"""
执行用时：
60 ms
, 在所有 Python3 提交中击败了
31.02%
的用户
内存消耗：
14.6 MB
, 在所有 Python3 提交中击败了
5.00%
的用户
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min_price)
        return dp[-1]


####题解关于动态规划解题的套路总结的不错

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/



    
