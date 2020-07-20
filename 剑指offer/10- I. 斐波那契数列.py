https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/mian-shi-ti-10-i-fei-bo-na-qi-shu-lie-dong-tai-gui/
# 由于 Python 中整形数字的大小限制 取决计算机的内存 （可理解为无限大），因此可不考虑大数越界问题。

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b       # 这种写法能保证a+b时，a的值还未更新。注意区别分两行写的效果
        return a % 1000000007
    
#时间复杂度：O(N)
#空间复杂度：O(1)

