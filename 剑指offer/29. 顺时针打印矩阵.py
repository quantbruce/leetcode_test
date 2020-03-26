class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        t, r, b, l, res = 0, len(matrix[0])-1, len(matrix)-1, 0, []
        while True:
            for i in range(l, r+1): res.append(matrix[t][i])
            t += 1
            if t>b: break
            for i in range(t, b+1): res.append(matrix[i][r])
            r -= 1
            if l>r: break
            for i in range(r, l-1, -1): res.append(matrix[b][i])
            b -= 1
            if t>b: break
            for i in range(b, t-1, -1): res.append(matrix[i][l])
            l += 1
            if l>r: break
        return res
        
        https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
