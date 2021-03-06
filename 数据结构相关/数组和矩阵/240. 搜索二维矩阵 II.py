编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。



"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
87.44%
的用户
内存消耗 :
18.3 MB
, 在所有 Python3 提交中击败了
10.00%
的用户
"""


#######左下角元素搜索法
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = len(matrix)-1, 0
        while i>=0 and j<=len(matrix[0])-1:
            if matrix[i][j]>target:
                i-=1
            elif matrix[i][j]<target:
                j+=1
            else:
                return True
        return False   
      
      

https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
