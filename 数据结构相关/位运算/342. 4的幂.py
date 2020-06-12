342. 4的幂
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？



###############方法1 My Methods
######tips: 本质上就是先排除特殊，和奇数情况，然后再逐个带值去套

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
56.41%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1: return True
        if num % 4!=0 or num&1!=0: return False
        i = 0
        while 4 ** i <= num:
            if 4**i == num:
                return True
            i+=1
        return False
        
# 我认为时间复杂度是 O(1) 。复杂度要把握“随着问题规模的增大，算法执行时间的增大速度”。对于本题，由于 n 是 int 值，因此是有限的。换句话说， 4**i 中的 i 最大可取 32，因此循环最多是 32 次，因此时间复杂度是 O(32) = O(1) 。

## 原理类似，官方的写法
"""
执行用时 :
32 ms
, 在所有 Python3 提交中击败了
97.37%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0: 
            return False
        while num % 4==0:
            num/=4
        return num==1

##############方法2：位运算
###tips：在2的幂的基础上进一步，看奇偶次。注意2进制转化成16进制，是四位一起看

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
56.42%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0

###########方法3 位运算+求模
####tips：拆解思路很巧妙

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
56.42%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and num&(num-1)==0 and num%3==1

https://leetcode-cn.com/problems/power-of-four/solution/4de-mi-by-leetcode/


