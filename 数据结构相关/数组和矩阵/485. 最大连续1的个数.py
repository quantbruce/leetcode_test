给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。




###############方法1
"""
执行用时 :
416 ms
, 在所有 Python3 提交中击败了
82.10%
的用户
内存消耗 :
13.9 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, max_num = 0, 0
        for i in range(len(nums)):
            if nums[i]==1:
                res+=1
                if res > max_num:
                    max_num = res
            else:
                res=0
        return max_num
        
https://leetcode-cn.com/problems/max-consecutive-ones/solution/xiao-bai-jian-dan-fang-fa-by-shuang-zi-zuo-de-yi-d/


################方法2
"""
执行用时 :
476 ms
, 在所有 Python3 提交中击败了
43.99%
的用户
内存消耗 :
14 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, res = 0, 0
        for i in range(len(nums)):
            if nums[i]==0:
                left = i+1
            res = max(res, i-left+1)
        return res

https://leetcode-cn.com/problems/max-consecutive-ones/solution/zui-da-lian-xu-1de-ge-shu-by-ml-zimingmeng/

