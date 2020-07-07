34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

####################方法1 线性扫描法

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
78.34%
的用户
内存消耗：
14.4 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-yi-/


#############方法2 两次复用 二分查找
######自己看了很久博客，时间花太多了8h...，不过还是自己最后写的，效率太低不满意！

"""
执行用时：
32 ms
, 在所有 Python3 提交中击败了
97.70%
的用户
内存消耗：
14.4 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        res = []
        # 找区间左端点
        left1, right1 = 0, len(nums)-1
        while left1 <= right1:
            mid1 = (left1+right1)//2
            if nums[mid1] < target: left1 = mid1 + 1
            elif nums[mid1] > target: right1 = mid1 - 1
            elif nums[mid1] == target: right1 = mid1 - 1
        if left1 >= len(nums) or nums[left1] != target:
            return [-1, -1]
        res.append(left1)
        # 找区间右端点
        left2, right2 = 0, len(nums)-1
        while left2 <= right2:
            mid2 = (left2 + right2)//2
            if nums[mid2] < target: left2 = mid2 + 1
            elif nums[mid2] > target: right2 = mid2 - 1
            elif nums[mid2] == target: left2 = mid2 + 1
        if right2 < 0 or nums[right2] != target:
            return [-1, -1]
        res.append(right2)
        return res

https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/er-fen-cha-zhao-xiang-jie

