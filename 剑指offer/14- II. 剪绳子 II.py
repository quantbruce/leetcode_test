####################循环取余与二分取余两种方法要掌握

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
84.91%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3: return n-1
        a,b = n//3,n%3
        if b==0: return 3**a % 1000000007
        elif b==1: return 3**(a-1)*4 % 1000000007
        else: return 3**a*2 % 1000000007



class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
        while a > 0: # 求 rem = 3^(a-1) % p
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0: return (rem * 3) % p # = 3^a % p
        if b == 1: return (rem * 4) % p # = 3^(a-1) * 4 % p
        return (rem * 6) % p # = 3^a * 2 % p


https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
