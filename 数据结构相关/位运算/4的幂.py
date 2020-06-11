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
        
        
##############方法2：






