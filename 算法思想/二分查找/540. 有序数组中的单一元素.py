540. 有序数组中的单一元素
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。



###############方法1 线性扫描法

"""
执行用时：
64 ms
, 在所有 Python3 提交中击败了
57.36%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

# 时间复杂度：O(N), 还不够好，未满足O(logN)
# 空间复杂度：O(1)
https://leetcode-cn.com/problems/single-element-in-a-sorted-array/solution/you-xu-shu-zu-zhong-de-dan-yi-yuan-su-by-leetcode/



###################方法2 二分查找法 
########即使该数组元素无序，该法仍然奏效

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
80.14%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2                    
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid] == nums[mid+1]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid] == nums[mid-1]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[hi] # 写 nums[lo] 也是对的，最后反正会重合

# 时间复杂度：O(logN)
# 空间复杂度：O(1)

https://leetcode-cn.com/problems/single-element-in-a-sorted-array/solution/you-xu-shu-zu-zhong-de-dan-yi-yuan-su-by-leetcode/



############# 方法3 仅对偶数索引进行二分搜索

## 代码更优雅，时间复杂度O(logN/2) 日后细究










