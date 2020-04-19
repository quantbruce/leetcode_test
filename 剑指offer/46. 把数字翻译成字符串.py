"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
79.55%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""


class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        s = str(num)
        for i in range(2, len(s)+1):
            tmp = s[i-2:i]
            c = a + b if "10"<=tmp<="25" else a    ## 有种斐波那契数列的味道，c的来源有两个
            b = a
            a = c
        return a

class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        s = str(num)
        for i in range(2, len(s)+1):
            tmp = s[i-2:i]
            a, b = (a + b if "10"<=tmp<="25" else a), a      # 这种写法与上面等价，除掉了中间变量c
        return a
        
        
   """
   执行用时 :
28 ms
, 在所有 Python3 提交中击败了
98.21%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
   """
    class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        y = num % 10
        while num!=0:
            num //= 10
            x = num % 10
            tmp = x*10 + y
            c = a+b if 10<=tmp<=25 else a
            a, b = c,a
            y = x 
        return a
