153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0


###########方法1: 不太通常的二分法 

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
88.21%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
6.67%
的用户
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[right] > nums[left]:
                return nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] > nums[mid+1]: # 区间长度为偶数 如[6, 7, 2, 3]  #这两种结束的条件不容易一下想到，记住了。
                return nums[mid+1]   
            if nums[mid-1] > nums[mid]: # 区间长度为奇数 如[7, 2, 3]
                return nums[mid]  
                
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-lie-shu-zu-zhong-de-zui-xi/ 
                
                
                
