538. 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
          
###########################方法1 递归回溯法

"""
执行用时：
84 ms
, 在所有 Python3 提交中击败了
54.82%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

class Solution:
    def __init__(self):
        self.total = 0  # 注意一定要这样定义个初始化方法，设置成全局变量才有效

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
        
        
https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/ba-er-cha-sou-suo-shu-zhuan-huan-wei-lei-jia-shu-3/






        
