#########My Methods 暴力法
"""
执行用时 :
620 ms
, 在所有 Python3 提交中击败了
25.28%
的用户
内存消耗 :
17.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res








