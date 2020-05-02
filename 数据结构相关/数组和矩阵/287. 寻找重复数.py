给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

1.不能更改原数组（假设数组是只读的）。
2.只能使用额外的 O(1) 的空间。
3.时间复杂度小于 O(n2) 。
4.数组中只有一个重复的数字，但它可能不止重复出现一次


"""
执行用时 :
80 ms
, 在所有 Python3 提交中击败了
83.06%
的用户
内存消耗 :
16 MB
, 在所有 Python3 提交中击败了
35.71%
的用户
"""

##########My Method(违反了不能改变原数组的要求)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
                

###########二分查找法(用时间换空间，少见套路)，该法满足题设，最优！

"""
执行用时 :
88 ms
, 在所有 Python3 提交中击败了
65.04%
的用户
内存消耗 :
15.9 MB
, 在所有 Python3 提交中击败了
35.71%
的用户
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            cnt=0
            for num in nums:
                if num<=mid:
                    cnt+=1
            if cnt > mid:
                right = mid
            else:
                left = mid+1
        return left


https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/



                
                
