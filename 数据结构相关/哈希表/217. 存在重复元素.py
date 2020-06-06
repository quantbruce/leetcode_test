217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 
 
#############My Methods 哈希表去重法

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i, item in enumerate(nums):
            if item not in dic:
                dic[item] = i
            else:
                return True
        return False
        
#######方法2，长度对比法，

## 利用set()去重，算是取巧了，不够底层

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
92.91%
的用户
内存消耗 :
19.1 MB
, 在所有 Python3 提交中击败了
16.00%
的用户
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) 
  
  
