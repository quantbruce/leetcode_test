######


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
