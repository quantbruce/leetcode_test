637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
注意：

节点值的范围在32位有符号整数范围内。


######################方法1： BFS 层序遍历

"""
执行用时：
60 ms
, 在所有 Python3 提交中击败了
81.84%
的用户
内存消耗：
16.1 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return 0
        res = []
        queue = [root]

        while queue:
            cur = []
            nxt = []
            for node in queue:
                cur.append(node.val)
                if node.left:
                    nxt.append(node.left) # 注意不是 node.left.val，nxt要与quque保持同样结构，内部都是装节点
                if node.right:
                    nxt.append(node.right)
            res.append(sum(cur)/len(cur))
            queue = nxt
        return res
        
https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/solution/er-cha-shu-xi-lie-637-er-cha-shu-de-ceng-ping-jun-/

################BFS的令一种写法

"""
执行用时：
60 ms
, 在所有 Python3 提交中击败了
82.02%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return 0
        queue = [root]
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            l = len(tmp)  # 统计这一层共有多少个节点，所以缩进的位置当然要放在这里
            if l>0:
                res.append(sum(tmp)/l)
        return res

        
   







