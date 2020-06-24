144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


##########################方法1：递归法

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
67.89%
的用户
内存消耗：
13.6 MB
, 在所有 Python3 提交中击败了
7.14%
的用户
"""

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return [root.val] +\
        self.preorderTraversal(root.left) +\
        self.preorderTraversal(root.right)



##########################方法二 非递归(迭代)

"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
86.71%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
7.14%
的用户
"""

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop() # 弹出栈顶元素,也就是最后一个，这里使用[]模拟栈结构
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)  # 先压进去的后弹出来，这样就确保了从左到右
                if node.left:
                    stack.append(node.left)
        return res

https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode/



