303. 区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。


##############方法1 暴力法
### 差点超时

"""
执行用时：
6920 ms
, 在所有 Python3 提交中击败了
9.53%
的用户
内存消耗：
16.9 MB
, 在所有 Python3 提交中击败了
24.14%
的用户
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for k in range(i, j+1):
            sum += self.data[k]
        return sum
        
#时间复杂度：每次查询的时间 O(n)O(n)，每个 sumrange 查询需要 O(n)O(n) 时间。
#空间复杂度：O(1)O(1)，请注意，data 是对 nums 的引用，不是它的副本。     
https://leetcode-cn.com/problems/range-sum-query-immutable/solution/qu-yu-he-jian-suo-shu-zu-bu-ke-bian-by-leetcode/ 
        


############方法二 缓存+动态规划

"""
执行用时：
104 ms
, 在所有 Python3 提交中击败了
64.07%
的用户
内存消耗：
17.2 MB
, 在所有 Python3 提交中击败了
20.69%
的用户
"""

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums: return 
        self.dp = [0] * (len(nums)+1) 
        self.dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            self.dp[i] = self.dp[i-1] + nums[i-1] # 体会下为什么dp[i]表示前i-1项的和，而不是前i项和。这个很关键
        
    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]

# 时间复杂度：O(n)，每次查询只需要O(1)
# 空间复杂度：O(n)
https://leetcode-cn.com/problems/range-sum-query-immutable/solution/huan-cun-dong-tai-gui-hua-python3-by-zhu_shi_fu/





        
        
