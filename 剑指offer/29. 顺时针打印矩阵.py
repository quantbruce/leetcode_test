class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        t, r, b, l, res = 0, len(matrix[0])-1, len(matrix)-1, 0, []
        while True:
            for i in range(l, r+1): res.append(matrix[t][i])
            t += 1
            if t>b: break              # t>b错写成t<b,记住t的初始下标是0，越往下下标越大
            for i in range(t, b+1): res.append(matrix[i][r])
            r -= 1
            if l>r: break
            for i in range(r, l-1, -1): res.append(matrix[b][i]) # range(r, l-1, -1)忘记下标是一路递减的，漏写了
            b -= 1
            if t>b: break
            for i in range(b, t-1, -1): res.append(matrix[i][l])
            l += 1
            if l>r: break
        return res
    
#时间复杂度: O(M*N)
#空间复杂度: O(1)
https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/

    
    
    
