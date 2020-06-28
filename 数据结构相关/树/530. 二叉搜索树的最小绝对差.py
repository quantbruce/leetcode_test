530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。


示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同


######################方法1 BST框架团灭法
########该法本质上是迭代法

"""
执行用时：
56 ms
, 在所有 Python3 提交中击败了
98.54%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        node = root
        min_val = float('inf') # 一开始让他永远取不到
        pre = -float('inf')  # 这里的设计要记住
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val - pre < min_val:  # 第一个根节点root，不让他进入if语句
                min_val = node.val - pre  # node.val就是当前节点值cur，pre是紧前节点值
            pre = node.val # pre = cur, 保证pre的移动
            node = node.right
        return min_val
        

https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/solution/zhong-xu-bian-li-tuan-mie-xi-lie-er-cha-sou-suo-sh/


############################方法2 递归法
############来源于CS-Notes, 但是转化python3过程还有些问题

private int minDiff = Integer.MAX_VALUE;
private TreeNode preNode = null;

public int getMinimumDifference(TreeNode root) {
    inOrder(root);
    return minDiff;
}

private void inOrder(TreeNode node) {
    if (node == null) return;
    inOrder(node.left);
    if (preNode != null) minDiff = Math.min(minDiff, node.val - preNode.val);
    preNode = node;
    inOrder(node.right);
}





