461. 汉明距离
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。


#############方法1, 调包法
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y)[2:].count('1')
 

#############方法2， 移位>>法

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
86.22%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
6.67%
的用户
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor = xor >> 1 # 注意这里不是else逻辑，因为统计完后，不管有没有都要右移一次位
        return distance
        
  
  ###############方法3 (最优方法) 布赖恩·克尼根算法
  
"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
86.22%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
6.67%
的用户
"""
        
class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
      xor = x ^ y
      distance = 0
      while xor:
         distance += 1
         xor = xor & (xor - 1) # 位运算tricks: n&(n-1) 去除 n 的位级表示中最低的那一位 1
      return distance


https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode/
