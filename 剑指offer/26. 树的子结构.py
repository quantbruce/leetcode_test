########方法1 Krahets 递归法
###很经典，记住思路框架，反复多看下PPT
###时间复杂度和空间复杂度有分析有些难。

"""
执行用时：
156 ms
, 在所有 Python3 提交中击败了
27.09%
的用户
内存消耗：
18.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/

    
    
