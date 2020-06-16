111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.


#########################方法1 递归法

"""
执行用时 :
64 ms
, 在所有 Python3 提交中击败了
31.59%
的用户
内存消耗 :
15.6 MB
, 在所有 Python3 提交中击败了
12.50%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l==0 or r==0: return l+r+1
        return min(l, r)+1


########## 同样的思路，也可以改成如下代码
class Solution:
    def minDepth(self, root: TreeNode) -> int: # 这个函数有三个return出口
        ## 该节点为空节点时
        if not root:
            return 0
        ## 让它去钻
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        ## 如果只有该节点只有一个儿子节点
        if not left or not right:
            return left + right + 1
        ## 当左右孩子节点都不为空时
        return min(left, right)+1 

https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/
