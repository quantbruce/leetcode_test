### 方法1 Inspired by 小抄

"""
暂时不理解总是报错，NameError memo is not defined 
"""

class Solution:
    memo = dict()
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        if root in memo.keys():
            return memo[root]
        do_it = root.val + \
            (0 if not root.left else rob(root.left.left) + rob(root.left.right)) +\
            (0 if not root.right else rob(root.right.left) + rob(root.right.right))
        not_do = rob(root.left) + rob(root.right)
        res = max(do_it, not_do)
        memo[root] = res
        return res
