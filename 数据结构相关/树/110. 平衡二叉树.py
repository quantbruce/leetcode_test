110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。


##############方法1 由下至上 (最优法) 

"""
执行用时 :
56 ms
, 在所有 Python3 提交中击败了
91.80%
的用户
内存消耗 :
17.5 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1 # 从下往上，某个局部节点的左右子树都不满足平衡树了，则整体必然不满足。这就是局部阻断效应，多体会下这代码
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right)+1 if abs(left-right)<=1 else -1
        
       
 https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/   
 
 
 
 ##########方法2，由上至下
 
"""
执行用时 :
64 ms
, 在所有 Python3 提交中击败了
73.96%
的用户
内存消耗 :
17.4 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
 """
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left)-self.depth(root.right))<=1 and\
              self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right))+1

 
 https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
 
 
 
 
    
