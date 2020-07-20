#######解法一：DFS(Deep Frist Search)

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):                                      # 不能重复访问已经访问过的元素，否则算个数相当于会重复计算
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)
#时间复杂度： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN)
#空间复杂度： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN)的额外空间。

#######解法一：BFS(Breadth Frist Search)

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited,  = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited: continue
            visited.add((i,j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)

#时间复杂度： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN)
#空间复杂度： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN)的额外空间。
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
