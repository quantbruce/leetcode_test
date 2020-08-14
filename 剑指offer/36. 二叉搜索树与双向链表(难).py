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

##################方法1 初始版
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            self.pre.right, cur.left = cur, self.pre # 修改引用
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        head = self.pre = ListNode(0) # 伪头节点  #这一点违反了题干要求，创建了新结点
        dfs(root)
        head = head.right 
        head.left, self.pre.right = self.pre, head
        return head
    
#时间复杂度：O(N)
#空间复杂度：O(N)

https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/

    
###################方法2 另写
"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
35.87%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return 
            dfs(cur.left) # cur的移动通过这两个递归
            if self.pre: # 这里未想到if-else这个分情况讨论，漏了
                self.pre.right, cur.left = cur, self.pre # 一边遍历，一边调整双向指针指向
            else:
                self.head = cur # cur的初始赋值，这里我漏了
            self.pre = cur # pre只能通过这条路平移迭代
            dfs(cur.right)
        
        if not root: return
        self.pre = None  # 本解法中， pre 相对于递归函数是全局变量，因此需要加 self~
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
    
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
#时间复杂度：O(N)
#空间复杂度：O(N)
