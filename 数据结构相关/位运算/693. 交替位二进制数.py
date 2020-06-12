693. 交替位二进制数
给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。

示例 1:

输入: 5
输出: True
解释:
5的二进制数是: 101
示例 2:

输入: 7
输出: False
解释:
7的二进制数是: 111
示例 3:

输入: 11
输出: False
解释:
11的二进制数是: 1011
 示例 4:

输入: 10
输出: True
解释:
10的二进制数是: 1010

#############方法1 移位异或再加1
###tips: 该方法技巧性较强

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
64.84%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = n^(n>>1) # 位运算优先，再计算异或^
        return tmp & (tmp + 1) == 0
        
https://leetcode-cn.com/problems/binary-number-with-alternating-bits/solution/python3-wei-yun-suan-by-jiren_zyz/       
 





