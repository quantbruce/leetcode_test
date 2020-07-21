###########方法1 位运算+&1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
    
#时间复杂度：O(logN)
#空间复杂度：O(1)


############方法2 
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

#时间复杂度 O(M)： n&(n−1) 操作仅有减法和与运算，占用O(1) ；设 M 为二进制数字 n 中 1 的个数，则需循环M次（每轮消去一个1），占用 O(M)。
#空间复杂度 O(1)： 变量 resres 使用常数大小额外空间。
https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
