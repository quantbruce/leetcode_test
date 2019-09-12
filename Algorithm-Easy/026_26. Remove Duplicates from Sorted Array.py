class Solution:
    def removeDuplicates(self, nums) :
        '''
        type nums: List[int]
        rtype: int
        '''
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:  # 体会
                count += 1
                nums[count] = nums[i]  #  把一开始不相等的count移到前面指定位置去
        return count + 1      # count 实际上就是记录了指针移动的次数，因为一开始index=0， 
                            # 所以返回长度的话 是len=count+1
