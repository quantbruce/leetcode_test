##################方法1 面试官骂人法

class Solution:
    def sumNums(self, n: int) -> int:
        return sum(list(range(1, n+1)))



###################方法2 Krahets 逻辑运算符短路效应法
"""
执行用时 :
52 ms
, 在所有 Python3 提交中击败了
52.73%
的用户
内存消耗 :
21.4 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
#时间复杂度：O(N) 需要开启N次递归函数
#空间复杂度：O(N) 递归深度
https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
