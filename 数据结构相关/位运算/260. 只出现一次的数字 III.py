260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

################方法1 哈希表法，
### tips: 思路是好，但空间复杂度不够

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
91.49%
的用户
内存消耗 :
15.1 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

from collections import Counter
class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]


#######也可以改写成这样
"""
执行用时 :
52 ms
, 在所有 Python3 提交中击败了
44.08%
的用户
内存消耗 :
15 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        return [i for i in hashmap if hashmap[i]==1]
        
        
      
        
        
        
        
        
        
        
