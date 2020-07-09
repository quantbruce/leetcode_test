413. 等差数列划分
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

 
示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。



###########方法1 动态规划法
####输入的数组A可以是整体等差，也可以是局部等差
###CS-Notes的笔记讲解的很好

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
99.25%
的用户
内存消耗：
13.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A: return 0
        dp = [0] * len(A)    
        total = 0
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                dp[i] = dp[i-1] + 1
                total += dp[i]
        return total

#dp[i] 表示以 A[i] 为结尾的等差递增子区间的个数。
#时间复杂度：O(N) 只需遍历数组 AA 一次，其大小为 nn。
#空间复杂度：O(N) 一维数组 dpdp 大小为 nn。
https://leetcode-cn.com/problems/arithmetic-slices/solution/deng-chai-shu-lie-hua-fen-by-leetcode/


###########方法2 对方法1的优化

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
97.37%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A: return 0
        dp = 0
        sum = 0
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                dp = dp + 1
                sum += dp
            else:
                dp = 0
        return sum

#dp[i] 表示以 A[i] 为结尾的等差递增子区间的个数。
#时间复杂度：O(N) 只需遍历数组 AA 一次，其大小为 nn。
#空间复杂度：O(1) 
https://leetcode-cn.com/problems/arithmetic-slices/solution/deng-chai-shu-lie-hua-fen-by-leetcode/



        
        
