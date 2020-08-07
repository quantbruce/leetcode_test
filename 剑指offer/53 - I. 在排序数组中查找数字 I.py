#########My Method

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if target == nums[i]:
                count+=1
        return count
#时间复杂度: O(N)
#空间复杂度: O(1)


############二分查找
####查两次，就相当于分别查出左右边界
class Solution:
    def search(self, nums: [int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i  # 没想到用两次while, 并且right=i也没考虑到

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        
        return right - left - 1

    
 ###########更展开详细的写法
class Solution:
    def search(self, nums: [int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            elif nums[m] == target: i = m + 1 # 向右缩，因此是在找右边界
            else: j = m - 1
        right = i

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            elif nums[m] == target: j = m - 1 # 向左缩，因此是在找左边界
            else: j = m - 1
        left = j
        
        return right - left - 1 
    
#时间复杂度：O(logN)
#空间复杂度：O(1)
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/

    
        
  
  
