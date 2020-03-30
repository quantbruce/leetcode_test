###########我的暴力解法(待验证)

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        nums = list(range(1, target-1))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if sum(nums[i:j+1])==target:
                    res.append(nums[i:j+1])   
        return res
        
        
#############################双指针算法(通向移动的双指针)
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i,j = 0,1
        res = []
        mid = target//2 + 2
        nums = list(range(1, mid))
        while i<=mid-1 and j<mid:
            total = sum(nums[i:j+1]) #如果是nums[i:j]也不会报错，只是会包含i与j重合的情况，计算成本高一些
            if total > target:
                i += 1
            elif total < target:
                j += 1
            else:
                res.append(nums[i:j+1]) #如果是nums[i:j]也不会报错，只是会包含i与j重合的情况，计算成本高一些
                i+=1
                j+=1
        return res
      
 https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/nei-cun-xiao-hao-153mzhan-sheng-100de-pythonyong-h/
   
