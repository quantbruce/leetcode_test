##################方法1 迭代法求解 
#### 样板戏。样板题。无需多言，记住！

"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
99.70%
的用户
内存消耗：
17.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return 
        stack = []  ## 暂时存储向右便遍历的顺序数，再从右逐个pop，以实现先进后出的效果。
        res = []
        while root or stack: ## root就是要遍历的二叉树节点，stack就是用来pop()到res中的栈
            while root:  
                stack.append(root)
                root = root.right
            root = stack.pop()
            res.append(root.val)
            if len(res)==k: return res[-1] # 第K大的节点和res[]的第K个数巧妙地联系到了一起
            root = root.left  # 没有左孩子节点，循环就不往右走
            
#时间复杂度：O(N) 注意其实是比N要小的，因为带有剪枝效应 
#空间复杂度：O(N)

https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/python-zhong-xu-bian-li-you-gen-zuo-by-janciswang/

    
################方法2 递归法求解 Krahets

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
    
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
    
    
