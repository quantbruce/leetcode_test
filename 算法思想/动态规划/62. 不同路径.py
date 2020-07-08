62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？


示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9




#############方法1 My Method
###这个思路自己还有些迷，也是醉了。。

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
89.93%
的用户
内存消耗：
13.6 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: dp[0][0] = 1 # 理解成在[0][0]这个坐标处，只有唯一的一种走法，
                elif i == 0 and j != 0: dp[i][j] = dp[i][j-1] # 可以理解成在边界时， 在[0][1]坐标处，走法和[0][0]处一样多
                elif i != 0 and j == 0: dp[i][j] = dp[i-1][j] # 同上类似，
                else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] # 在非边界点时，走法来源只有来源于上面和左边两个方向
        return dp[-1][-1]
        
#时间复杂度： O(M*N)
#空间复杂度： O(M*N)  # 还存在继续进一步优化的可行性
#思路来源 64 题
 

################方法2 数学 组合数法
### 时间复杂度和空间复杂还没搞清楚

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
51.27%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
   
#时间复杂度：
#空间复杂度：
   
https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
   
   
########方法3 动态规划法 另类写法 + 不断优化空间复杂度
   
   
https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
   
   
