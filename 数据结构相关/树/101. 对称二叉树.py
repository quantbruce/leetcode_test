101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

########################################  你可以运用递归和迭代两种方法解决这个问题吗？


############方法1： 复制同一颗树对比对比的递归思路

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        return s.val==t.val and self.isMirror(s.left, t.right) and\
        self.isMirror(s.right, t.left)


https://leetcode-cn.com/problems/symmetric-tree/solution/hua-jie-suan-fa-101-dui-cheng-er-cha-shu-by-guanpe/
