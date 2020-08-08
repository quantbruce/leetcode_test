##########构建L[i],R[i]

"""
执行用时 :
72 ms
, 在所有 Python3 提交中击败了
86.97%
的用户
内存消耗 :
22.4 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        L, R = [1] * n, [1] * n
        
        for i in range(1, n):
            L[i] = L[i - 1] * a[i - 1]
            
        for j in reversed(range(n - 1)): # for j in range(n-2, -1, -1):
            R[j] = R[j + 1] * a[j + 1]
            
        for i in range(n):
            L[i] = L[i] * R[i]
        return L
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/liang-tang-bian-li-by-z1m/

    
    
#################方法2 Krahets法






