94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


#############################方法1：递归法

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
43.44%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
7.84%
的用户
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        return self.inorderTraversal(root.left) +\
               [root.val] +\
               self.inorderTraversal(root.right)
               
               

###########################BFS 所有迭代框架法
###这是一种解这种题的通用框架，很有味道，必须掌握。

"""
执行用时：
28 ms
, 在所有 Python3 提交中击败了
99.05%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
7.84%
的用户
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == white:
                stack.append((white, node.right))  ## 改变下这个if条件语句中的三个顺序，就可以分别实现前中后遍历
                stack.append((gray, node))
                stack.append((white, node.left))
            else:
                res.append(node.val)
        return res


https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/


###########底下的解答区高赞回答，还可以将方法2进一步让代码更简化
#####思路和方法2本质上是一样的


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.val, node.left]) # node.right和node.left是TreeNode类型(表明还未访问过)，而node.val是int类型(代表已经访问过)
            elif isinstance(node, int):
                res.append(node)
        return res

https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/204119
               
