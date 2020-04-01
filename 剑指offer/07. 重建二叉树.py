############################直观的递推法

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        #创建当前节点
        node = TreeNode(preorder[0]) 
        #在中序遍历中查找第一个节点的位置
        index = inorder.index(preorder[0]) 
        # 划分左右子树
        left_pre = preorder[1:index+1]
        left_in = inorder[:index]
        right_pre = preorder[index+1:]
        right_in = inorder[index+1:]
        # 遍历创建子树
        node.left = self.buildTree(left_pre, left_in)
        node.right = self.buildTree(right_pre, right_in)
        # 返回当前节点
        return node


https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/pythonti-jie-qing-xi-di-gui-si-lu-by-xiao-xue-66/
