53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

################方法1 贪心算法

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
56.68%
的用户
内存消耗：
14.5 MB
, 在所有 Python3 提交中击败了
6.35%
的用户
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i]) # 如果之前的cur_sum<0 直接扔掉不考虑
            max_sum = max(max_sum, cur_sum)
        return max_sum

https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/

################方法2 动态规划

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
89.62%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
6.35%
的用户
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
