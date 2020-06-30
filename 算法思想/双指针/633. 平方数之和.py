633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False

##################方法1 二分查找  (官方)
#######代码部分样例没有通过，还没搞懂原因

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(left, right, n):
            if left>right: return False
            mid = left + (right-left)//2
            if mid*mid == n: return True
            if mid*mid > n:
                binary_search(left, mid-1, n)
            else:binary_search(mid+1, right, n)

        a = 0
        while a*a <= c:
            b = c - a*a
            a += 1 
            if binary_search(0, b, b):
                return True
        return False
        
        
        
        
###############方法2  根号法

"""
执行用时：
236 ms
, 在所有 Python3 提交中击败了
62.77%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
20.00%
的用户
"""
        
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a*a<=c:
            b = math.sqrt(c-a*a)
            a+=1
            if b==int(b):
                return True
        return False
        
时间复杂度：O(c^0.5)
空间复杂度：O(1)
https://leetcode-cn.com/problems/sum-of-square-numbers/solution/ping-fang-shu-zhi-he-by-leetcode/
        
        
############方法3 费马平方和定理
###主要利用了 费马平方和定理，日后再细啃


