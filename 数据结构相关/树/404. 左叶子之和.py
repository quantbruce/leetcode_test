404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

####################方法1: 递归法
####该法出现了标志位flag, 设计的很巧妙，掌握这个套路。

"""
执行用时 :
28 ms
, 在所有 Python3 提交中击败了
99.86%
的用户
内存消耗 :
14.3 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.helper(root, False)
    
    def helper(self, root, flag):
        if not root: return 0
        leave = 0
        if (flag and not root.left and not root.right):
            leave += root.val
        left = self.helper(root.left, True)
        right = self.helper(root.right, False)
        return left + right + leave


https://leetcode-cn.com/problems/sum-of-left-leaves/solution/javadi-gui-yu-die-dai-shi-xian-si-lu-by-ggb2312/
