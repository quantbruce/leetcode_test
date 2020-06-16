100. 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

  
##################方法1 递归法
#####tips: 时间复杂度和空间复杂度还没分析，要再细究下。
          
"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
86.44%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
7.14%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return p.val==q.val and self.isSameTree(p.left, q.left) and\
        self.isSameTree(p.right, q.right)


######该解法的母体思想
https://leetcode-cn.com/problems/subtree-of-another-tree/solution/dui-cheng-mei-pan-duan-zi-shu-vs-pan-duan-xiang-de/


