226. 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。


################方法1 DFS 递归法

"""
执行用时 :
32 ms
, 在所有 Python3 提交中击败了
95.92%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
5.26%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
###############方法2 BFS 层序遍历法

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
86.55%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
5.26%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        from collections import deque
        dq = deque([root])
        while dq:
            node = dq.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return root

https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/




