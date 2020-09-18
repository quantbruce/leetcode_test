https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/pythonti-jie-san-chong-fang-fa-by-xiao-xue-66/

###################方法1 排序思路
"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
90.27%
的用户
内存消耗：
23.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return pre
            pre = nums[i]
            
#时间复杂度: O(N*log(N))     
#空间复杂度: O(1)        
    
    
################方法2 My Methods 字典去重法

"""
执行用时：
68 ms
, 在所有 Python3 提交中击败了
24.67%
的用户
内存消耗：
28.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用
"""
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        for k, val in enumerate(nums):
            if d[val]!=1:
                return val
            
        #for val in nums:  其实这样写就可以了，上面enumerate是多余的在此处
        #   if d[val]!=1:
        #        return val

#时间复杂度：O(N) 
#空间复杂度：O(N)
   
            
            
            
