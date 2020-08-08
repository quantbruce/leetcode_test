############难点在于要把各种情况考虑的面面俱到


#####################方法1 Krahets之前的方法
"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
51.28%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip() # 删除首尾空格  # 空间复杂度 O(N)
        if not str: return 0 # 字符串为空则直接返回
        res, i, sign, max_int = 0, 1, 1, 2 ** 31 - 1
        if str[0] == '-': sign = -1 # 保存负号
        elif str[0] != '+': i = 0 # 若无符号位，则需从 i = 0 开始数字拼接, elif换成if就会错
        for c in str[i:]:
            if not '0' <= c <= '9' : break # 遇到非数字的字符则跳出
            res = 10 * res + ord(c) - ord('0') # 数字拼接, c不用加引号，0要加！
            if res > max_int: return max_int if sign == 1 else -max_int - 1 # 数字越界处理
        return sign * res
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/solution/mian-shi-ti-67-ba-zi-fu-chuan-zhuan-huan-cheng-z-4/

    

######################Krahets 优化上述方法后的方法2

