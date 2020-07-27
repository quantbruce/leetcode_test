"""
执行用时 :
156 ms
, 在所有 Python3 提交中击败了
92.34%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

###############################方法1  DP
###细节，要注意不等号取值的方向
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1, n): # 因为dp[0]=1(默认设定),第一个数永远是1，不管什么丑数序列
                              # 如果是range(1, n+1),想想当n=10时, 最大元素下标也就是9.刚好是range(1, n)
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2, n3 ,n5)
            if dp[i] == n2: a+=1  # 下一轮的每个dp[i]都是由上一轮的三个n2,n3,n5比较取最小而得
            if dp[i] == n3: b+=1  # dp[i]只可能来源于这三种情况，后面两个if不能写作elif, 因为很多时候，n2,n3,n5之间会存在相等，
            if dp[i] == n5: c+=1  # 则此时所有相当的情况，对应下标都要加1
        return dp[-1]

