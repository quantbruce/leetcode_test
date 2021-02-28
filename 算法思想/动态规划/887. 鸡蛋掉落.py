### 方法1. 朴素动态规划
inspired by 小抄

"""
超时
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            if K==1: return N
            if N==0: return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('INF')
            for i in range(1, N+1):     
                res = min(res, max(dp(K-1, i-1), dp(K, N-i))+1 )
            memo[(K, N)] = res
            return res
        return dp(K, N)

# 时间复杂度：O(KN^2)
# 空间复杂度：O(KN)

### 方法2 二分搜索+动态规划 inspired by 小抄

"""
执行用时：3004 ms, 在所有 Python3 提交中击败了7.47%的用户
内存消耗：43.4 MB, 在所有 Python3 提交中击败了16.42%的用户
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            if K==1: return N
            if N==0: return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('INF')
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo+hi)//2
                broken = dp(K-1, mid-1)
                not_broken = dp(K, N-mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken+1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken+1)
            memo[(K,N)] = res
            return res
        return dp(K, N)

# 时间复杂度：O(KNlogN)
# 空间复杂度：O(KN)


### 方法3 动态规划他法定义： inspired by 小抄

"""
执行用时：68 ms, 在所有 Python3 提交中击败了85.66%的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了69.92%的用户
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0]*(N+1) for i in range(K+1)] # 行列坐标别弄反了, 体会
        m = 0
        while dp[K][m] < N:  # 还可以进一步压缩成1维空间，日后细究！
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        return m

# 时间复杂度：O(KN)
# 空间复杂度：O(KN)
