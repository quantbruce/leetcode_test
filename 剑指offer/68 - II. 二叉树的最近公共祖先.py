# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack_1 = []
        stack_2 = []
        def dfs(root, node, stack):
            if not root:
                return False
            stack.append(root)
            if root.val == node.val:
                return True          
            if (dfs(root.left, node, stack) or dfs(root.right, node, stack)):
                return True
            stack.pop()
            
        dfs(root, p, stack_1)
        dfs(root, q, stack_2)
        i = 0
        while i < len(stack_1) and i<len(stack_2) and stack_1[i] == stack_2[i]:
            result = stack_1[i]
            i += 1
        return result


https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/pythonti-jie-bu-tong-si-kao-fang-shi-ying-he-mian-/

