70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶


##############方法1 递归法

"""
超时
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            if n == 1: return 1
            elif n == 2: return 2
            return helper(n-1) + helper(n-2)
        return helper(n)
        
# 时间复杂度：O(2^n)  # 这个两个有些难理解...在细究下！多看下官方解答视频
# 空间复杂度: O(n) 
https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/

##############方法2 记忆化递归

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
64.84%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
20.59%
的用户
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] *(n+1) # n+1项，最开始的第0项不算
        def helper(n, memo):
            if memo[n] > 0: return memo[n] # 如果之前已计算过memo[n], 则直接返回，这样可以保证爬到各层台阶的数目只会被计算一次，将时间复杂度减少到O(N)
            if n == 1: memo[n] = 1
            elif n == 2: memo[n] = 2
            else:
                memo[n] = helper(n-1, memo) + helper(n-2, memo) 
            return memo[n]
        return helper(n, memo)

# 时间复杂度: O(N)
# 空间复杂度: O(N) 

https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/


###############方法3 动态规划法

"""
执行用时：
32 ms
, 在所有 Python3 提交中击败了
95.08%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
20.59%
的用户
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        dp = [0 for _ in range(n+1)]
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 时间复杂度： O(N)
# 空间复杂度： O(N)

https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/


############方法4 斐波那契数列

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
85.01%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
20.59%
的用户
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        first, second = 1, 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second

# 时间复杂度: O(N)
# 空间复杂度: O(1)

https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/


###########方法5 通项公式矩阵形式法 日后细究
### 该法本质上是运用数学

https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/





