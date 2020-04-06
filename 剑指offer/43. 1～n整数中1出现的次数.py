######
"""
执行用时 :
32 ms
, 在所有 Python3 提交中击败了
90.55%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""


class Solution(object):
    def countDigitOne(self, n: int) -> int:
            if n <= 0: return 0
            nums = str(n)
            high = int(nums[0])
            power = pow(10, len(nums)-1)
            last = n - high*power
            if high == 1:
                return  self.countDigitOne(power-1) + last + 1 + self.countDigitOne(last)
            else:
                return  self.countDigitOne(power-1)*high + power + self.countDigitOne(last)
                
                
                
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/pythondi-gui-by-rainiee-pan/
