145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


##########################方法一： 递归法

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
43.29%
的用户
内存消耗：
13.6 MB
, 在所有 Python3 提交中击败了
7.41%
的用户
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.postorderTraversal(root.left) +\
               self.postorderTraversal(root.right) +\
               [root.val]


##########################方法二： 迭代法(非递归)

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
43.29%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
7.41%
的用户
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left) # 注意这里的左右顺序, 自己在纸上笔画下，认真看下题解。
            if node.right:
                stack.append(node.right)

        return res[::-1]


https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode/







               
               
               
               
               
