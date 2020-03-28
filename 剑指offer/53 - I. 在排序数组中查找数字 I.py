#########My Method

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if target == nums[i]:
                count+=1
        return count
        


############二分查找
class Solution:
    def search(self, nums: [int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        
        return right - left - 1


链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/

        
  
  
