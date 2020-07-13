494. 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。


示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
 

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。


####################方法1 暴力枚举法
"""
python3超时
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.count = 0
        def helper(nums, i, sum_, S):
            if i == len(nums):
                if sum_ == S:
                    self.count += 1
                return 
            else:
                helper(nums, i+1, sum_+nums[i], S)
                helper(nums, i+1, sum_-nums[i], S)
        helper(nums, 0, 0, S)
        return self.count
        
# 时间复杂度：O(2**N)
# 空间复杂度：O(N)
https://leetcode-cn.com/problems/target-sum/solution/mu-biao-he-by-leetcode/


################方法2 动态规划法












