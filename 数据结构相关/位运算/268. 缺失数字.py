268. 缺失数字
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

##################方法1 求和做差法，逼妖怪现原形
### tips: 这个方法不足之处在于，只是从数学原理角度出发，没有用到数据结构的知识
"""
执行用时 :
52 ms
, 在所有 Python3 提交中击败了
66.25%
的用户
内存消耗 :
14.8 MB
, 在所有 Python3 提交中击败了
6.06%
的用户
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = sum([i for i in range(len(nums)+1)])  ## 这个空间复杂度怎么算？ O(N)么
        return sum2 - sum1
        
        
        
        
###################方法2 排序法

"""
执行用时 :
60 ms
, 在所有 Python3 提交中击败了
43.37%
的用户
内存消耗 :
14.5 MB
, 在所有 Python3 提交中击败了
12.12%
的用户
"""

 class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0 

        for i in range(1, len(nums)):
            expected_num = nums[i-1]+1
            if nums[i]!=expected_num:
                return expected_num
 
 ###################方法3 哈希表
 """
 执行用时 :
56 ms
, 在所有 Python3 提交中击败了
53.68%
的用户
内存消耗 :
15.1 MB
, 在所有 Python3 提交中击败了
6.06%
的用户
 """
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in range(len(nums)+1):
            if num not in nums_set:
                return num
 
 ###################方法4 位运算 (最优方法)
 
"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
80.37%
的用户
内存消耗 :
14.7 MB
, 在所有 Python3 提交中击败了
6.06%
的用户
"""
 
 class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    
 https://leetcode-cn.com/problems/missing-number/solution/que-shi-shu-zi-by-leetcode/

        
        
        
        
        
