给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4


"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
84.42%
的用户
内存消耗 :
15.2 MB
, 在所有 Python3 提交中击败了
10.53%
的用户
"""

##############这个解法(位运算)可以当作定理去记

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for num in nums:
            single_num ^= num
        return single_num

https://leetcode-cn.com/problems/set-mismatch/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-f/




