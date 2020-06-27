235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。


###################方法1 递归法

"""
执行用时：
96 ms
, 在所有 Python3 提交中击败了
73.91%
的用户
内存消耗：
17.7 MB
, 在所有 Python3 提交中击败了
9.09%
的用户
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # parent_val = root.val 这样方便理解点，但性能稍微低点
        # p_val = p.val
        # q_val = q.val

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)  # 这里的left和right先后顺序无所谓
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            
            
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian--2/ 




###########################方法2 迭代法 
##### 这个迭代法有点特殊，由于没有回溯过程，所以不需要用到stack
##### 仔细多体会下

"""
执行用时：
92 ms
, 在所有 Python3 提交中击败了
86.91%
的用户
内存消耗：
17.9 MB
, 在所有 Python3 提交中击败了
9.09%
的用户
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        node = root
        
        while node:
            parent_val = node.val
            if p_val < parent_val and q_val < parent_val:
                node = node.left
            elif p_val > parent_val and q_val > parent_val:
                node = node.right
            else:
                return node


https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian--2/
            
