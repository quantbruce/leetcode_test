给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


###############法1
"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
65.51%
的用户
内存消耗 :
14.4 MB
, 在所有 Python3 提交中击败了
7.41%
的用户
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """    
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count>0:
                nums[i-count], nums[i]=nums[i], 0
        return nums

https://leetcode-cn.com/problems/move-zeroes/solution/pythonti-san-chong-jie-fa-kuai-lai-kan-by-sunfox/
