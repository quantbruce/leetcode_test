####################方法1 递归法

"""
执行用时 :
88 ms
, 在所有 Python3 提交中击败了
88.56%
的用户
内存消耗 :
17.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            min_, max_ = q.val, p.val
        else:
            min_, max_ = p.val, q.val  
                  
        result = []
        def search(root, p, q):
            if root.val >= p and root.val <= q:
                result.append(root)
                return
            if root.val > p and root.val > q:
                search(root.left, p, q)
            else:
                search(root.right, p, q)
        
        search(root, min_, max_)
        
        return result[0]           


https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/pythonti-jie-jian-dan-yi-dong-dfs-by-xiao-xue-66-2/

    
###################方法2 迭代法

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val < q.val and root.val < p.val:  ### 细节，这两个if的顺序不能换，是right在前left在后，二叉树DFS遍历的感觉
                root = root.right
            (el)if root.val > q.val and root.val > p.val:  ## 这里的if改成elif 两者right/left先后顺序便无所谓了
                root = root.left
            else:
                return root
            
#时间复杂度：O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/pythonti-jie-jian-dan-yi-dong-dfs-by-xiao-xue-66-2/

##################方法3 递归法

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
    
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/pythonti-jie-jian-dan-yi-dong-dfs-by-xiao-xue-66-2/



