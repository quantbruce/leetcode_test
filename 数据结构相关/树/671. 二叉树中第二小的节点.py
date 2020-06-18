671. 二叉树中第二小的节点
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:

输入: 
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
示例 2:

输入: 
    2
   / \
  2   2

输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。



#####################方法1 DFS+集合记录法

"""
执行用时 :
28 ms
, 在所有 Python3 提交中击败了
98.51%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        s = set()
        def helper(root):
            if not root: return
            s.add(root.val) 
            helper(root.left)
            helper(root.right) # 这里的DFS递归更多只是为了把所有树节点的值塞到集合里去，所以不需要返回什么值
        helper(root)
        return sorted(s)[1] if len(s)>1 else -1
        
        
######################方法2  迭代法？
##### 与方法1在性能上差不多

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
85.35%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        return self.helper(root, root.val)
    def helper(self, root, min_val): # min_val其实就是最上面的根节点值
        if not root: return -1
        if root.val > min_val:
            return root.val
        left = self.helper(root.left, min_val)
        right = self.helper(root.right, min_val)
        if left == -1:  ## left可以返回root.val，也可以返回-1
            return right
        if right == -1: ## right可以返回root.val, 也可以返回-1
            return left
        return min(left, right)  ## 来到这一步，必然是left,和right都不为-1, 都有各自返回的root.val
        
        
#### 解答在下方评论区
https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/solution/er-cha-shu-zhong-di-er-xiao-de-jie-dian-by-leetcod/ 
        
        
