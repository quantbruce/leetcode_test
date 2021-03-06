572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

###############方法1 递归法
########这种代码简洁优美，效率还很高，值得学习内化。但是时间复杂度和空间复杂度还没分析好，要再细究下。

"""
执行用时 :
244 ms
, 在所有 Python3 提交中击败了
75.19%
的用户
内存消耗 :
14.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or\  # 注意这里后两个是  isSubtree(), 之前这里老写错！理解并体会。 
        self.isSubtree(s.right,t)

    def isSameTree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        return s.val==t.val and self.isSameTree(s.left, t.left) and\
        self.isSameTree(s.right, t.right)
        
 https://leetcode-cn.com/problems/subtree-of-another-tree/solution/dui-cheng-mei-pan-duan-zi-shu-vs-pan-duan-xiang-de/   
     
