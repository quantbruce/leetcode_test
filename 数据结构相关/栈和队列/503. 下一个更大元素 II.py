503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。


#############方法1，单调栈法(栈底的元素永远最大，从下往上单调递减)

"""
执行用时 :
292 ms
, 在所有 Python3 提交中击败了
52.55%
的用户
内存消耗 :
15 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for i in range(len(nums))]  # 提前准备好-1
        stack = [] # 用于保存nums中符合要求的下标

        for i in range(2*len(nums)): # 循环，所以需要两次
            index = i % len(nums)  # 取余破循环，体会
            while stack and nums[stack[-1]] < nums[index]:  # 但栈不会空，且刚才栈顶元素<最新比较元素nums[index]
                res[stack.pop()] = nums[index] #stack.pop()会返回单个删除的元素，即满足上述条件的下标
            if i < len(nums): # 确保单调栈的关键，如果没有这个限定，循环完一次后，接着stack中又会出现同样下标index, 这样整个栈就不在是单调栈了
                stack.append(index)
        return res
