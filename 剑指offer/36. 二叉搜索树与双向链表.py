"""
执行用时 :
32 ms
, 在所有 Python3 提交中击败了
98.58%
的用户
内存消耗 :
14.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            self.pre.right, cur.left = cur, self.pre # 修改引用
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        head = self.pre = ListNode(0) # 伪头节点
        dfs(root)
        head = head.right
        head.left, self.pre.right = self.pre, head
        return head


https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
