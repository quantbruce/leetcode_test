167. 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


#############方法1 双指针法
####只有双指针法利用了有序这个条件，
####时间复杂度: O(N)
####空间复杂度: O(1)

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
89.55%
的用户
内存消耗：
14.2 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:             
                return [left+1, right+1]
                
自己写的，思路和官方解答一样           
                
                
