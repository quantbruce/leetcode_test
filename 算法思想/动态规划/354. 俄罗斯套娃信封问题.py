方法1.
inspired by labuladong 算法小抄第二章
"""
执行用时：
8184 ms
, 在所有 Python3 提交中击败了
31.55%
的用户
内存消耗：
17 MB
, 在所有 Python3 提交中击败了
23.00%
的用户
"""

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lengthLIS(nums):
            numsLen = len(nums)
            dp = [1] * numsLen
            for i in range(numsLen):
                for j in range(0, i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            res = 0
            for i in range(numsLen):
                res = max(res, dp[i])
            return res

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height = []
        for i in range(len(envelopes)):
            height.append(envelopes[i][1])
        return lengthLIS(height)

      
