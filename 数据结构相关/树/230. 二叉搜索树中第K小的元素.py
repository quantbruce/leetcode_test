230. 二叉搜索树中第K小的元素
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3

################# 进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

#########方法1 中序遍历DFS (官方)

"""
执行用时：
64 ms
, 在所有 Python3 提交中击败了
73.15%
的用户
内存消耗：
17.7 MB
, 在所有 Python3 提交中击败了
7.14%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        return dfs(root)[k-1]
        
        
https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/solution/er-cha-sou-suo-shu-zhong-di-kxiao-de-yuan-su-by-le/
        
      
#########################方法2 BFS法  (中序遍历）
######这个及时止损BFS区别于一般套路，要好好掌握，
 
"""
执行用时：
64 ms
, 在所有 Python3 提交中击败了
73.15%
的用户
内存消耗：
17.8 MB
, 在所有 Python3 提交中击败了
7.14%
的用户
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
   
   
# 复杂度分析
# 时间复杂度：\mathcal{O}(H + k)O(H+k)，其中 HH 指的是树的高度，由于我们开始遍历之前，要先向下达到叶，当树是一个平衡树时：复杂度为 \mathcal{O}(\log N + k)O(logN+k)。当树是一个不平衡树时：复杂度为 \mathcal{O}(N + k)O(N+k)，此时所有的节点都在左子树。
# 空间复杂度：\mathcal{O}(H + k)O(H+k)。当树是一个平衡树时：\mathcal{O}(\log N + k)O(logN+k)。当树是一个非平衡树时：\mathcal{O}(N + k)O(N+k)

https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/solution/er-cha-sou-suo-shu-zhong-di-kxiao-de-yuan-su-by-le/

   
      
      
