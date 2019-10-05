#### My method
ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ls2 = []

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        ls2.append(sum(ls[i:j+1]))
print(max(ls2))


#### Better way
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max)
        return global_max
