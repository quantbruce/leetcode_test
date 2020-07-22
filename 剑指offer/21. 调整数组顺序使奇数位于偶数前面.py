########我自己的思路，分成两个数组再相加

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        self.A, self.B = [], []
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                self.A.append(nums[i])
            else:
                self.B.append(nums[i])
        res = self.A + self.B
        return res
#时间复杂度：O(N)
#空间复杂度：O(N)

#############方法2 双指针法
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            while i < j and nums[i]&1: i += 1
            while i < j and nums[j]&1==0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
#时间复杂度：O(N)
#空间复杂度：O(1)
