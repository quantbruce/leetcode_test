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

#时间复杂度：O(1)
#空间复杂度：O(1)


#############方法2 考虑大数越界
"""
Python 代码（第三栏）： 由于语言特性，理论上 Python 中的变量取值范围由系统内存大小决定（无限大），因此在 Python 中其实不用考虑大数越界问题。
"""

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
    
#时间复杂度：O(log(N))
#空间复杂度：O(1)
https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/

