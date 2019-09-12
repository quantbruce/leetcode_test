#### My Frist Way (think by myself!!! yes!)

class Solution:
    def searchInsert(self, nums, target):
        '''
        :type nums: List[int]
        :target: int
        :rtype: int
        '''
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            for i in range(len(nums)):
                if nums[i] < target < nums[i+1]:
                    return i+1


if __name__ == '__main__':
    a = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    print(a.searchInsert(nums, target))
    
    
    
    #### Better way
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums)-1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i]>=target:
                    return i
    
