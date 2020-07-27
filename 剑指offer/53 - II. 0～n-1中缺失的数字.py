###########方法1 数学法
###观察一下做差即可
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum([i for i in range(len(nums)+1)])
        sum2 = sum(nums)
        return sum1 - sum2
    
#时间复杂度：O(N) ??????????
#空间复杂度：O(1)



#####有序数组查询---有限考虑二分查找法

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i # 容易写错成nums[i], 稍微试想下，nums[i]就是整个数组中缺少的那个数，你还想引用他，这里面压根就没有。所以自然是i
#时间复杂度：O(logN)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
