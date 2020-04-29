在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。


"""
执行用时 :
116 ms
, 在所有 Python3 提交中击败了
69.11%
的用户
内存消耗 :
14.4 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:   
        m, n = len(nums), len(nums[0])
        if m*n!=r*c: 
            return nums
        res = [j for i in nums for j in i]
        return [res[i:i+c] for i in range(0, len(res), c)]

https://leetcode-cn.com/problems/reshape-the-matrix/solution/pythonqie-pian-hao-yong-by-2558260433/


