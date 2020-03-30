###########我的暴力解法(只是从理论上可行，实际上会超时！！)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        res = []
        while target-nums[i] not in nums:
            i+=1
        res.append(nums[i])
        # while len(res)<2:
        for j in range(i+1, len(nums)):
            if target-nums[j]!=res[0]:
                pass
            else:
                res.append(nums[j])
                break
        return res
        
 
 ###################双指针法解决排序数组
 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target: j -= 1
            elif s < target: i += 1
            else: return nums[i], nums[j]
        return []


链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/mian-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/
