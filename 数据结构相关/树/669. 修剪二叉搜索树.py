669. 修剪二叉搜索树
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例 1:

输入: 
    1
   / \
  0   2

  L = 1
  R = 2

输出: 
    1
      \
       2
示例 2:

输入: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

输出: 
      3
     / 
   2   
  /
 1
 

####################方法1 递归法 官方

"""
执行用时：
72 ms
, 在所有 Python3 提交中击败了
31.27%
的用户
内存消耗：
17.8 MB
, 在所有 Python3 提交中击败了
20.00%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node: 
                return None
            if node.val < L:
                return trim(node.right)
            elif node.val > R:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)
 

 https://leetcode-cn.com/problems/trim-a-binary-search-tree/solution/xiu-jian-er-cha-sou-suo-shu-by-leetcode/
 
 
 
