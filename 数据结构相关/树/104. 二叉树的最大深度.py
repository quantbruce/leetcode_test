104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

###############方法1 DFS(深度优先搜索)
####关于空间复杂度的分析，值得好好琢磨下。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        while not root:
            return 0
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
        return max(left, right) + 1  # 因为算的是结点数，而不是线段数。所以要+1

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode/


################方法2 BFS(用到了队列)

"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
88.12%
的用户
内存消耗 :
15 MB
, 在所有 Python3 提交中击败了
5.55%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque
        if not root: return 0
        q = deque([root])
        res = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1 # 注意res的缩进位置，是弄完每一层所有节点，就增加一次
        return res

#时间复杂度O(n)
#空间复杂度O(n)


        
