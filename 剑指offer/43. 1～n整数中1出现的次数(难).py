################方法1 Krahets 拆分所有情况法
#####这个解法以及思路很经典，值得记住！
#####反复多看题解PPT


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10,  0
        while high != 0 or cur != 0:  # 这个连接条件是or, 容易写错成and
            if cur == 0: res += digit*high
            elif cur == 1: res += digit*high + low + 1 #这几项res结果都带 += 累加效应
            else: res += (high + 1) * digit
            low += cur * digit  
            cur = high % 10   # cur与high的顺序要记住谁先更新，默写错过
            high //= 10
            digit *= 10
        return res
# 时间复杂度O(log n)：循环内的计算操作使用O(1)时间；循环次数为数字n的位数，即 \log_{10}{n}log 10n ，因此循环使用O(logn) 时间。
# 空间复杂度 O(1)： 几个变量使用常数大小的额外空间。
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/



############# 方法2 
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
