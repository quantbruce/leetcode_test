
##############方法1 递归法
"""
执行用时 :
120 ms
, 在所有 Python3 提交中击败了
95.35%
的用户
内存消耗 :
18.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set() # 对应是第x位的字符集合
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，固定此位为 c[i] 
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res
    
#时间复杂度: O(N!)
#空间复杂度：O(N**2)


https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
