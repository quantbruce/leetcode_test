###################方法1 动态规划
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
    
#时间复杂度：O(M*N)
#空间复杂度：O(1)



#################方法2 优化后的动态规划
"""
执行用时 :
52 ms
, 在所有 Python3 提交中击败了
91.16%
的用户
内存消耗 :
14.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for j in range(1, len(grid[0])): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, len(grid)): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
    
#时间复杂度：O(M*N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/

