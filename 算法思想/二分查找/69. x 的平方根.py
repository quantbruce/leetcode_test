69. x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
     

################方法1 调包法
###本质上就是数学上的转化

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
97.72%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
6.06%
的用户
"""

import math      
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * log(x)))
        return ans + 1 if (ans + 1)**2<=x else ans

https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/


###########方法2 二分查找

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
93.47%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
6.06%
的用户
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r: # =号可以包含x=0的特殊情况
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/



###########方法3 牛顿法 最优
####日后细究

https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/


