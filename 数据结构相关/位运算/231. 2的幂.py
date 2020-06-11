231. 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false


################方法1 My Method 直男法(最容易想到的方法)

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
62.60%
的用户
内存消耗 :
13.5 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        elif n&1==1: return False
        i=1
        while 2**i <= n:
            if 2**i==n:
                return True
            i+=1
        return False

时间复杂度: O(nlog(n))错了，是O（1），因为emmm 我认为时间复杂度是 O(1) 。复杂度要把握“随着问题规模的增大，算法执行时间的增大速度”。对于本题，由于 n 是 int 值，因此是有限的。换句话说， 2**i 中的 i 最大可取 32，因此循环最多是 32 次，因此时间复杂度是 O(32) = O(1) 。
空间复杂度: O(1)


##############方法2 n&(n-1)==0 归纳法 (最优方法)

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
81.43%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0


https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/

