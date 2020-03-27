######My Method
#####排序取中思路
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        return nums[int(len(nums)/2)]
        
        
 ######
 class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/

