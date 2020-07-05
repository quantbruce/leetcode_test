665. 非递减数列
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
 

说明：

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5

################方法1 一次遍历法

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
70.41%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if i+1 < len(nums) and i-2>=0: # 数组不越界
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]: # 特殊情况易漏想
                        return False
            if count>1: return False
        return True
        
        
https://leetcode-cn.com/problems/non-decreasing-array/solution/python3xiang-jie-bu-gai-bian-shu-zu-yuan-su-zhi-ch/

     
