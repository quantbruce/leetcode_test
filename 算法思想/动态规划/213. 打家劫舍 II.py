213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
89.03%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        def helper(nums: List[int]):
            first, second = 0, 0 # 这个地方不能写成first, second = nums[0], max(nums[0], nums[1]) 因为nums此时只是一个形参，又没有预定义为数组，
            for i in range(len(nums)): # 故写成0，0草稿纸上笔画下，这样赋初值去迭代算最后结果也是一样的
                first, second = second, max(first + nums[i], second)  # i 换成 num 这里不写成索引形式更好，与for num in nums: 搭配
            return second
        return max(helper(nums[1:]), helper(nums[:-1])) if len(nums)!=1 else nums[0]
        
# 时间复杂度: O(N)
# 空间复杂度: O(1)
https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/

"""
补充：
该解法问题转化还有些未解释清楚，因为对于一个环来说，如果求最大值，存在首尾两个节点都不取的情况；
但为什么问题可以转化为求两个队列呢？
因为对于上述情况，即首尾都不取时，它的最大值肯定小于等于只去掉首或者只去掉尾的队列。
即f（n1,n2,n3）<=f(n1,n2,n3,n4)
"""     


### 方法2 动态规划
# Inspired by 小抄

"""
执行用时：40 ms, 在所有 Python3 提交中击败了60.63%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了76.80%的用户
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums, start, end):
            dp_i, dp_i_1, dp_i_2 = 0, 0, 0
            for i in range(end, start-1, -1):
                dp_i = max(dp_i_1, nums[i] + dp_i_2)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i
        n = len(nums)
        if n==1: return nums[0]
        return max(robRange(nums, 0, n-2), robRange(nums, 1, n-1))

# 时间复杂度：O(N)
# 空间复杂度：O(N)














