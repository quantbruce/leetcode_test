1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
执行用时 :
60 ms
, 在所有 Python3 提交中击败了
70.23%
的用户
内存消耗 :
15 MB
, 在所有 Python3 提交中击败了
5.48%
的用户
"""

def two_sum(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    dct = {}
    for i, n in enumerate(nums):
        if target - n in dct:
            return [dct[target - n], i]
        dct[n] = i


https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/



实测三种判断方式各运行100万次用时（win10 python3.7.3）：

key in dict 用时 1.088 秒
dict.get(key) 用时 1.294 秒
dict[key] 用时 1.01 秒
显然第一种和第三种都很快，速度相差不大，第二种要比其他写法慢很多，采用第一种写法更加直观。
