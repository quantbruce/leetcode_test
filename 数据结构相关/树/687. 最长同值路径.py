687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。




####################方法1 

"""
执行用时 :
456 ms
, 在所有 Python3 提交中击败了
87.69%
的用户
内存消耗 :
17.4 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:            
        self.ans = 0 # ans要放在这作为全局变量

        def arrow_length(root):
            if not root: return 0
            left_length = arrow_length(root.left)  # 见多了, 这个是常见的二叉树计数套路
            right_length = arrow_length(root.right)

            left_arrow = right_arrow = 0
            if root.left and root.val == root.left.val:
                left_arrow = left_length + 1
            if root.right and root.val == root.right.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow) # 保持ans每次递归后得到更新
            return max(left_arrow, right_arrow) # 该轮返回的结果

        arrow_length(root)
        return self.ans
        
        
  https://leetcode-cn.com/problems/longest-univalue-path/solution/zui-chang-tong-zhi-lu-jing-by-leetcode/
  
  
