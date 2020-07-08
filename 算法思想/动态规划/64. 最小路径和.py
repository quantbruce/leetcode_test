64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

##############方法1 动态规划
###非常典型的动态规划题

"""
执行用时：
56 ms
, 在所有 Python3 提交中击败了
82.40%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue # 此处是continue, 体会下
                elif i == 0 and j != 0: grid[i][j] = grid[i][j-1] + grid[i][j] # 要学会考虑边界
                elif i != 0 and j == 0: grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j-1]+grid[i][j], grid[i-1][j]+grid[i][j])
        return grid[-1][-1]

# 时间复杂度: O(M*N)
# 空间复杂度: O(1)

https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
        
        
