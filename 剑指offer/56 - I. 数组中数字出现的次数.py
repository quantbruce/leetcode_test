##################自己独立思考下，很快解答出的一题，而且接近双百，再接再厉。保持进步！

"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
96.73%
的用户
内存消耗 :
14.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]]+=1 
                            
        res = []
        for key, value in dic.items():
            if value == 1:
                res.append(key)
        return res


