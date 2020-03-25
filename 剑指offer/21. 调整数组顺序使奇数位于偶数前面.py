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
