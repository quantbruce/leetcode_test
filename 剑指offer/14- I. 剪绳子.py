class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        elif b == 1: return int(math.pow(3, a - 1) * 4) # 这里写错过，改成elif也不会报错,
        return int(math.pow(3, a) * 2)
    
#时间复杂度：O(1)
#空间复杂度：O(1)

解法：
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
证明：
https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-shu-xue-fang-fa-han-wan-zheng-t/

