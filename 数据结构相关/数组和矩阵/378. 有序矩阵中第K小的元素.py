给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。



#####################法1(My Method)  本质是暴力法、时间复杂度太高了，空间复杂度也大
"""
执行用时 :
212 ms
, 在所有 Python3 提交中击败了
77.14%
的用户
内存消耗 :
19.6 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = [j for i in matrix for j in i]
        res.sort()
        return res[k-1]
        
#############方法二(更高效的暴力法)

"""
执行用时 :
200 ms
, 在所有 Python3 提交中击败了
90.84%
的用户
内存消耗 :
19.6 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis=[]
        for l in matrix:
            lis+=l  ##############体会：列表不要只会append, 还可以用加号。不要思维固化，这样效率会高很多
        lis.sort()
      
        return lis[k-1]

      
      
################方法3  二分法

################方法4  堆排序法


