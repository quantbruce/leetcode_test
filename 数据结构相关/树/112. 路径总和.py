112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


###############方法1 递归法
"""
执行用时 :
56 ms
, 在所有 Python3 提交中击败了
62.28%
的用户
内存消耗 :
15.6 MB
, 在所有 Python3 提交中击败了
6.67%
的用户
"""

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode/


#################方法2 迭代法

"""
执行用时 :
64 ms
, 在所有 Python3 提交中击败了
26.80%
的用户
内存消耗 :
15.4 MB
, 在所有 Python3 提交中击败了
6.67%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        de=[(root, sum-root.val)]
        while de:
            node, cur_sum = de.pop()
            if not node.left and not node.right and cur_sum == 0: ## 到达了叶子节点
                return True
            if node.right:                                         ## node.right与node.left的先后顺序可以调换
                de.append((node.right, cur_sum - node.right.val))
            if node.left:
                de.append((node.left, cur_sum - node.left.val))
        return False 


https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode/














