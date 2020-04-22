"""
执行用时 :
84 ms
, 在所有 Python3 提交中击败了
72.64%
的用户
内存消耗 :
14.3 MB
, 在所有 Python3 提交中击败了
6.67%
的用户
"""
##########DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!='0':
                    count+=1
                    self.dfs(grid,i,j)
        return count

    def dfs(self, grid, i, j):    # 因为由上面的循环可知，i的取值是0~len(grid)-1, 所以i=len(grid)时就越界了，j同理。
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
 

https://blog.csdn.net/starmoth/article/details/88607289
    
    
    
##############################BFS
   class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def numIslands(self, grid: List[List[str]]) -> int: 
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()                  
                        for direction in self.directions:
                            new_i = cur_x + direction[0]         ##这里存疑
                            new_j = cur_y + direction[1]         ##这里存疑            
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True
        return count
    
    
    https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
