######My Method
#####排序取中思路
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        return nums[int(len(nums)/2)] #通过观察规律可得，满足这样条件的数必过nums中点
#时间复杂度: O(N)
#空间复杂度：O(1)
        
###################摩尔投票法，有些技巧性
########新颖 务必掌握

 class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

#时间复杂度: O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/


##########方法3 My Method

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
92.82%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
def majorityElement(self, nums: List[int]) -> int:
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 0
        else:
            dic[num] += 1
    for num, times in dic.items():
        if times>=len(nums)//2:
            return num
        
#时间复杂度: O(N)
#空间复杂度：O(N)
        
    
