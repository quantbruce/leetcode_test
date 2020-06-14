617. 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。

##############方法1 递归法
"""
执行用时 :
116 ms
, 在所有 Python3 提交中击败了
32.02%
的用户
内存消耗 :
14.9 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        
        t1.left=self.mergeTrees(t1.left, t2.left)
        t1.right=self.mergeTrees(t1.right, t2.right)
        return t1
        
        
##############方法2 迭代法
        
"""
执行用时 :
96 ms
, 在所有 Python3 提交中击败了
83.99%
的用户
内存消耗 :
14.8 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
 """       
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        
        stack = [[t1, t2]]
        while stack:
            t = stack.pop()
            if not t[0] or not t[1]: # t[0], t[1]两者只要有一个为空
                continue
            t[0].val += t[1].val

            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append([t[0].left, t[1].left])
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append([t[0].right, t[1].right])
        return t1
