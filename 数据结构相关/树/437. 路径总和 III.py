437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11


##################方法1：双层递归法

###该法效率较低，因为递归层数过深，需要再优化

"""
执行用时 :
728 ms
, 在所有 Python3 提交中击败了
53.99%
的用户
内存消耗 :
14.6 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        if not root: return 0
        it = self.countPath(root, sum)
        it_left = self.pathSum(root.left, sum)
        it_right = self.pathSum(root.right, sum)
            
        return it + it_left + it_right
        
    def countPath(self, root, sum):
        if not root: return 0
        sum -= root.val
        return (1 if sum==0 else 0)+self.countPath(root.left, sum)+\
        self.countPath(root.right, sum)


https://leetcode-cn.com/problems/path-sum-iii/solution/437lu-jing-zong-he-iii-di-gui-fang-shi-by-ming-zhi/
https://leetcode-cn.com/problems/path-sum-iii/solution/hot-100-437lu-jing-zong-he-iii-python3-li-jie-di-g/
















  
