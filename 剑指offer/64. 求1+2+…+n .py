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


https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
