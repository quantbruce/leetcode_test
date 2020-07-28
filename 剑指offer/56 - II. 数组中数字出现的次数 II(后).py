##################自己独立思考下，很快解答出的一题，而且效果还凑合，再接再厉。保持进步！
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


####进行简化后
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        
        for k,v in dic.items():
            if v==1:
                return k
#时间复杂度：O(N)
#空间复杂度：O(N)
            
    
#######################方法2 Krahets  位运算 + 有限状态自动机，清晰图解
###日后细究



#时间复杂度：O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
    
    
