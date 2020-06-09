136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

#################位运算，

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for num in nums:
            single_num ^= num # 只要list[]中成对的元素，不论什么顺序，最后一系列连续异或^运算，都会变为0，而0与任何数异或等于任何数，所以最后落单的数
           # 必然 会被揪出来        
        return single_num
