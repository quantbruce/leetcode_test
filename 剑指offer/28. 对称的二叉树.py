class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        res = True  # 为了考虑当root为空时的情况
        if root:
           res = self.helper(root.left, root.right)
        return res  # return 的位置，不管是不是空，都会执行这一条语句。
    
    def helper(self,A,B):
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        if A.val != B.val:
            return False
        return self.helper(A.left,B.right) and self.helper(A.right,B.left)
        
https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/cyu-pythonliang-chong-jie-fa-shi-xian-di-gui-yu-di/
        

###############方法1 最优雅 镜像法(本质就是递归法)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(node1,node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False
            return node1.val==node2.val and isMirror(node1.left, node2.right) and\
            isMirror(node1.right, node2.left)
        return isMirror(root, root)
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/symmetric-tree/solution/hua-jie-suan-fa-101-dui-cheng-er-cha-shu-by-guanpe/
    
################方法2 迭代法 (理解原理)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not node1 and not node2: continue
            if not node1 or not node2 or node1.val!=node2.val: return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/symmetric-tree/solution/di-gui-die-dai-bi-xu-miao-dong-by-sweetiee/
