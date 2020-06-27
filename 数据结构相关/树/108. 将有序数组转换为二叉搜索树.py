108. 将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
 
 #################方法1 递归法 
 ##### 均分后取区间左端点，这题答案不唯一，所以测试未必能通过，但提交可以通过
 ##### 好好体会下几种方法的差别

"""
执行用时：
60 ms
, 在所有 Python3 提交中击败了
61.79%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
9.52%
的用户
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left>right:
                return None
            p = (left + right) // 2  # 均分后取左端点
            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)
            return root
        return helper(0, len(nums)-1)


https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-15/
