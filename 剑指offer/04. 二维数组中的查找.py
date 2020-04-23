https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/

左下角标志数法，清晰图解

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j= len(matrix)-1,0
        while i>=0 and j< len(matrix[0]):  #j不取等号是由于，如果i和j都取了等号，则就没有留给任何空间给target了，因为matrix[i][j]能取到最右上角元素
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False
