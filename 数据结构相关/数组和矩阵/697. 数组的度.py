给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
注意:

nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。




"""
执行用时 :
276 ms
, 在所有 Python3 提交中击败了
78.80%
的用户
内存消耗 :
15 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

############
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num]=i
            right[num]=i
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num]-left[num]+1)
        return ans


https://leetcode-cn.com/problems/degree-of-an-array
