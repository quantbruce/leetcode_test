#### Michelle way
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for i in range(n):            # 这种方式解决斐波那契数列是很有套路的，记住了
            prev, current = current, prev + current
        return current
        
   
