416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.


#################方法1 动态规划法 (二维)
####二维还可以进一步优化为1维

"""
执行用时：
2432 ms
, 在所有 Python3 提交中击败了
18.46%
的用户
内存消耗：
17.6 MB
, 在所有 Python3 提交中击败了
11.11%
的用户
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:              
        sum_ = 0
        for num in nums:
            sum_ += num
        if sum_ & 1 != 0: return False
        n = len(nums)
        sum_ = sum_ // 2
        dp = [[False for _ in range(sum_+1)] for _ in range(n+1)]  # base case 就是 dp[..][0] = true 和 dp[0][..] = false，
        for i in range(n+1):                                       #   因为背包没有空间的时候，就相当于装满了，而当没有物品可选择的时候，肯定没办法装满背包。
            dp[i][0] = True # 恰好能将背包装满时，就是True. 要理解本题题意
        
        for i in range(1, n+1):
            for j in range(1, sum_+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]  # 注意下标，这个地方老犯错
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[n][sum_] # 改成dp[-1][-1]也是可行的

#时间复杂度：O(n*sum_)
#空间复杂度：O(n*sum_)
https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/bei-bao-zi-ji     
        


###############方法2 动态规划 (一维)     


"""
执行用时：
1424 ms
, 在所有 Python3 提交中击败了
55.36%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = 0
        n = len(nums)
        for num in nums:
            sum_ += num
        if sum_ & 1 != 0: return False
        sum_ //= 2
        dp = [False for _ in range(sum_+1)]
        dp[0] = True  # 
        for i in range(n):
            for j in range(sum_, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
              
        return dp[sum_]
       
#时间复杂度：O(n*sum_)
#空间复杂度：O(sum_)
https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/bei-bao-zi-ji

