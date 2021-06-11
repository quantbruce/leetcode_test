//方法1
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) 
    {
        int i = matrix.length-1, j = 0;
        while(i >= 0 && j <= matrix[0].length-1)
        {
            if(matrix[i][j] > target)
                i -= 1;
            else if(matrix[i][j] < target)
                j += 1;
            else
                return true;
        }
        return false;
    }
}
