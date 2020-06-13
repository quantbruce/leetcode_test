543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。



################## 方法1：深度优先搜索

"""
执行用时 :
60 ms
, 在所有 Python3 提交中击败了
51.51%
的用户
内存消耗 :
15.8 MB
, 在所有 Python3 提交中击败了
22.22%
的用户
"""


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1  # 两个节点之间的距离，最小也必然是1，所以这里是1而不是0
        def depth(node):
            # 访问到空节点了，返回0
            if not node: return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L+R+1)  # L+R+1算的是节点数
            # 返回该节点为根的子树的深度
            return max(L, R) + 1  # 也就是返回该节点左右子树的最大深度+1

        depth(root)  # 让这个函数自己跑，它会算出更新之后的ans
        return self.ans - 1  # 直径求得是节点之间得线段数，细节要注意区分


https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/
