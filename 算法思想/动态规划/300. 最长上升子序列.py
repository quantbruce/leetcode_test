300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


################方法1 动态规划

"""
执行用时：
1268 ms
, 在所有 Python3 提交中击败了
38.83%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
7.89%
的用户
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for i in range(len(nums))]        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) # 输出 dp[-1]可能是错的，反例：[1,3,6,7,9,4,10,5,6]
        
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/     


################方法2 动态规划的优化     

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
91.06%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
7.89%
的用户
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i+j)//2
                if tails[m] < num: 
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if res == j: res += 1
        return res
    
#时间复杂度: O(N*log(N))
#空间复杂度：O(N)
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/

