class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, last = 0, len(nums) - 1
        while i <= last:   ## 建立首尾两个指针，相对移动。一旦i指针<last指针，就退出循环。
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]  # 体会思想，只要val 元素和nums[i]就把num[i]放到后面去，实际上就是这个交换的作用。可以
                last -= 1                                   # 确保要删除的元素都排在后面，而通过last指针前移，可以只访问前面指定的未被删除的元素。
            else:
                i += 1
        return last + 1

if __name__ == "__main__":
    print(Solution().removeElement([1, 2, 3, 4, 2, 3], 2))
    
    
    
    #### My imitation
    class Solution:
    def removeElement(self, nums, val):
        '''
        type: List[int]
        val: int
        rtype: list[int]
        '''
        i, last = 0, len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        print('nums length: ', last + 1)
        print('new nums after remove val: ', nums[:last+1])
        return

if __name__ == "__main__":
    Solution().removeElement([1, 2, 3, 4, 2, 3], 2)
    
