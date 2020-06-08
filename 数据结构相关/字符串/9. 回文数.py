9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。


########我的方法 双指针法

"""
执行用时 :
80 ms
, 在所有 Python3 提交中击败了
80.02%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
5.88%
的用户
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        i, j = 0, len(x)-1
        while i < j:
            if x[i] != x[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        
        
        
