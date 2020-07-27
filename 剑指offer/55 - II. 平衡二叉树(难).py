# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1   ####left==-1的-1是来自于上一轮的下面else -1 返回的-1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right)+1 if abs(left-right)<=1 else -1
        
        return recur(root)!=-1

    https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/
