"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
36.44%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # if len(nums)!=5: return False  ## 这行代码可有可不有，都不会报错！
        nums.sort()
        count0 = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
        start=count0
        if nums[-1]-nums[start]>4:
            return False
        else:
            if(len(set(nums[start:])))!=len(nums[start:]):
                return False
            else:
                return True     

https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/bu-neng-you-kong-xi-bu-neng-you-zhong-fu-by-keyian/

####对上述代码简化之后

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if len(nums) != 5: return False
        nums.sort()
        count0 = nums.count(0)
        start = count0
        if nums[-1] - nums[start] > 4:
            return False
        if len(nums[start:])!=len(set(nums[start:])):
            return False
        return True
#时间复杂度：O(N*logN)  ???????
#空间复杂度：O(1)



################方法2 Krahets 线性遍历+集合法  最优

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        ma, mi = 0, 14
        repeat = set()
        for num in nums:
            if num==0: continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat: return False
            repeat.add(num)
        return ma-mi<5

#时间复杂度：O(N)
#空间复杂度：O(N)



################方法3 排序 + 遍历 Krahets














