https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/

左下角标志数法，清晰图解

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j= len(matrix)-1,0 #这里不用加 if not matrix: return False 因为，matrix为空不报错，但matrix为空时引用matrix[0]就会报错，此时while第一个条件就不满足，更轮不到后面报错了。
        while i>=0 and j< len(matrix[0]):  # 关于i,j的边界取值问题。因为 i 的取值范围是 [0, len(matrix) - 1] ， j 的取值范围是 [0, len(matrix[0]) - 1] ，可以对照一下~ 比如一个长度为 n 的数组，索引取值范围是 [0, n-1]
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False

    
 #### 右上角法    
class Solution:
def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix: return False # 加了这行代码
    i, j = 0, len(matrix[0])-1
    while i <= len(matrix)-1 and j >= 0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        else:
            return True
    return False
