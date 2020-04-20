"""
执行用时 :
68 ms
, 在所有 Python3 提交中击败了
73.69%
的用户
内存消耗 :
14.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        res=[]
        for key, value in dic.items():
            if value == 1:
                res.append(key)
        return res[0]


