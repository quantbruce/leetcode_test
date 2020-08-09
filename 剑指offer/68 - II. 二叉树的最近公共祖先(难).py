# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack_p = []  # 用来储存从上往下遍历找到p的轨迹
        stack_q = []  # 同理q
        def dfs(root, node, stack):  # 这个函数递归寻找子树用的很巧妙，反复多体会！
            if not root: return False
            stack.append(root)
            if root.val == node.val: return True
            if dfs(root.left, node, stack) or dfs(root.right, node, stack): # or是因为，没在根节点的左子树找到，还有可能在右子树找到, 这个地方老写错，return....
                return True
            stack.pop() # 表示p,q都没在二叉树中找到的情形, 因为这个stack的长度后面要用到
        
        dfs(root, p, stack_p)
        dfs(root, q, stack_q)
        i= 0
        while i<len(stack_p) and i<len(stack_q) and stack_p[i]==stack_q[i]:
            res = stack_p[i]
            i+=1
        return res # res当下的值总会覆盖之前的值，确保更新。res注意不是list
    
#时间复杂度：O(N) ???
#空间复杂度：O(N) ??????
  
https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/pythonti-jie-bu-tong-si-kao-fang-shi-ying-he-mian-/

######################感觉方法2 更好
#####比较费解，关于left以及right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root==p or root==q:  #这几种情况合并的代码写的漂亮
            return root
        left = self.lowestCommonAncestor(root.left, p, q) # left和right返回有4种组合，空、非空etc
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:  #就是应对上面left和right的几种组合而设置的
            return right
        if not right:
            return left
        else:
            return root
        
#时间复杂度：O(N) ???????
#空间复杂度：O(N) ???????
https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/pythonti-jie-bu-tong-si-kao-fang-shi-ying-he-mian-/
