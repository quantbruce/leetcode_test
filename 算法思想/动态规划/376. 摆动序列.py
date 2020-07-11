376. 摆动序列
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

输入: [1,7,4,9,2,5]
输出: 6 
解释: 整个序列均为摆动序列。
示例 2:

输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
示例 3:

输入: [1,2,3,4,5,6,7,8,9]
输出: 2
进阶:
你能否用 O(n) 时间复杂度完成此题?

################方法1 动态规划
### 虽然可以AC, 但时间复杂度偏高，还不够完美，不能满足进阶要求。

"""
执行用时：
212 ms
, 在所有 Python3 提交中击败了
17.56%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        up, down = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)
        return max(up[-1], down[-1])
        
#时间复杂度：O(N**2)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/wiggle-subsequence/solution/bai-dong-xu-lie-by-leetcode/    



##############方法2 线性动态规划 更优
###时间复杂度可以优化到 O(N)

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
78.54%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 2: return len(nums)
        up, down = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):   # 这里范围是从1开始，老容易写错！！！
            if nums[i-1] < nums[i]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i-1] > nums[i]:
                down[i] = up[i-1] + 1 
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1])
        
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/wiggle-subsequence/solution/bai-dong-xu-lie-by-leetcode/


#####################方法3： 空间优化的动态规划

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
91.43%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
        
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 2: return len(nums)
        up, down = 1, 1
        for i in range(1, len(nums)): # 这里范围是从1开始，老容易写错！！！
            if nums[i-1] < nums[i]:
                up = down + 1
            elif nums[i-1] > nums[i]:
                down = up + 1
        return max(up, down)
        
 #时间复杂度：O(N)
 #空间复杂度：O(1)
https://leetcode-cn.com/problems/wiggle-subsequence/solution/bai-dong-xu-lie-by-leetcode/
        

        
