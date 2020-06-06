128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

###########方法一：哈希表

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
76.17%
的用户
内存消耗 :
14.6 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if num-1 not in nums_set: #num没有前驱时，才可以以num为起点。否则就是低效徒劳
                current_num = num 
                current_streak = 1

                while current_num+1 in nums_set:
                    current_num += 1
                    current_streak += 1    

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/

