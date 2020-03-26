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
        
        
