"""
执行用时 :
36 ms
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

https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
