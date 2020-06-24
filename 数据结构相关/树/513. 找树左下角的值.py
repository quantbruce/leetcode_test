513. 找树左下角的值
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7


注意: 您可以假设树（即给定的根节点）不为 NULL。

"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
96.16%
的用户
内存消耗：
16.1 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
       
####题解来源于：就是CS-Note目录对应笔记



######################方法2 DFS

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
87.43%
的用户
内存消耗：
16.5 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not root: return
            if depth>self.maxdepth:
                self.maxdepth = depth
                self.res = root.val  # 确保res永远保存的是最深的节点值，下面两个递归顺序用来确定向左还是向右，最终取到左边的结果还是右边的结果
            dfs(root.left, depth+1)  # 递归，层数往下面钻，这两个顺序交换下，就是找到右节点去了。自己体会
            dfs(root.right, depth+1)
            
        self.maxdepth, self.res = -1, 0
        dfs(root, 0)
        return  self.res

https://leetcode-cn.com/problems/find-bottom-left-tree-value/solution/513dfsshen-du-di-gui-bian-bfsyan-du-xun-huan-bian-/











