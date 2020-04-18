"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
79.79%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 首先判断target是几位数，用digits表示
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字
        if idx == 0:  # 也即n%digits刚好可以被整除，实际上idx就是指向上一个number的最后一位，也就是digits位。
            idx = digits  # idx==0这种情况(刚好可以被整除比较特殊点)，需要另外分析。
        number = 1
        for i in range(1, digits): # 就是1位数，2位数，3位数最开始的那个数
            number *= 10       
        if idx == digits:
            number += n // digits - 1   # 与上面25行代码对应，可以被整除，number要向前面移一位
        else:
            number += n // digits
        # 找到target中对应的数字
        for i in range(idx,digits):
            number //= 10
        return number % 10

https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/zhe-shi-yi-dao-shu-xue-ti-ge-zhao-gui-lu-by-z1m/
