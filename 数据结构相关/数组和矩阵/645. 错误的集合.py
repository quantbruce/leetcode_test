集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

1.给定数组的长度范围是 [2, 10000]。
2.给定的数组是无序的。


"""
执行用时 :
228 ms
, 在所有 Python3 提交中击败了
90.38%
的用户
内存消耗 :
15.2 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))
        return [(sum(nums)-S), len(nums)*(len(nums)+1)//2-S]
        
 class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        err = sum(nums) - sum(set(nums))                # 找到重复出现的整数
        re = set(range(1, len(nums)+1)) - set(nums)     # 找到丢失的整数
        return [err, sum(re)] 







