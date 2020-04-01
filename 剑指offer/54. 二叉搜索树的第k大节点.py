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
            if len(res)==k: return res[-1]
            root = root.left  # 没有左孩子节点，循环就不往右走
        return


https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/python-zhong-xu-bian-li-you-gen-zuo-by-janciswang/
