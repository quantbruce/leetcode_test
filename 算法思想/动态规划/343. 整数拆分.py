343. 整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

############ 方法1 数学求导最值法

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
81.86%
的用户
内存消耗：
13.5 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

import math
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n-1
        a, b = n//3, n % 3
        if b == 0: return int(math.pow(3, a))
        elif b == 1: return int(math.pow(3, a-1) * 4)
        return int(math.pow(3, a) * 2)
        
#时间复杂度 O(1)： 仅有求整、求余、次方运算。
求整和求余运算：查阅资料，提到不超过机器数的整数可以看作是 O(1)O(1) ；
幂运算：查阅资料，提到浮点取幂为 O(1)O(1) 。
#空间复杂度 O(1)： a 和 b 使用常数大小额外空间。
https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
  

############方法2 递归法 
#### 普通递归会超时，加个装饰器就很快了

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
26.77%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

class Solution:
    @lru_cache() # 这个装饰器，这个装饰器实现了备忘的功能，是一项优化技术，把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i),i * (n - i)))
        return res

https://leetcode-cn.com/problems/integer-break/solution/ba-yi-ba-zhe-chong-ti-de-wai-tao-343-zheng-shu-cha/
https://zhuanlan.zhihu.com/p/27643991 # 装饰器讲解


############ 方法3 递归记忆法

https://leetcode-cn.com/problems/integer-break/solution/tan-xin-xuan-ze-xing-zhi-de-jian-dan-zheng-ming-py/


############ 方法4 动态归纳法

"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
44.08%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)] #为什么长度是n+1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        return dp[n]
        
#时间复杂度：O(N**2)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/integer-break/solution/tan-xin-xuan-ze-xing-zhi-de-jian-dan-zheng-ming-py/


########### 方法5 动态规划法 优化

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
64.49%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        dp[0] = 0 # dp[0]也等于1的话，则n=3时，就返回3，而正确答案是2
        for i in range(3, n+1):
            dp[i] = max(max(i-1, dp[i-1])*1,
                        max(i-2, dp[i-2])*2,
                        max(i-3, dp[i-3])*3)
        return dp[n]

#时间复杂度：O(N）
#空间复杂度：O(N)
https://leetcode-cn.com/problems/integer-break/solution/tan-xin-xuan-ze-xing-zhi-de-jian-dan-zheng-ming-py/

    
    
########### 方法6 滚动数组法 最优

#时间复杂度：O(N)
#空间复杂度: O(1)
https://leetcode-cn.com/problems/integer-break/solution/tan-xin-xuan-ze-xing-zhi-de-jian-dan-zheng-ming-py/
    
    
    
    
