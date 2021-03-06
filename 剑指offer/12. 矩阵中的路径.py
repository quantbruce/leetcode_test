##########这题很经典，一定要结合那个动画来看来理解

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False # 注意是or连接
            if k == len(word) - 1: return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1) # 这几项顺序可以打乱的
            board[i][j] = tmp
            return res

        for i in range(len(board)):  ######因为起点任意，所以可以i*j种遍历方式。
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False

#时间复杂度：O(3^k * M*N)
#空间复杂度：O(K), 最坏情况O(MN)
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
