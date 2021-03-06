501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

##############进阶：
你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）


#################方法1 BFS + 字典统计法
####这个方法是最直观的，也是最容易想的，但是效率略低，且不满足进阶要求。
####时间复杂度和空间复杂度需进一步细究
####答案可能不止一个，也就是有多个值出现的次数一样多。

"""
执行用时：
68 ms
, 在所有 Python3 提交中击败了
77.30%
的用户
内存消耗：
17.7 MB
, 在所有 Python3 提交中击败了
20.00%
的用户
"""

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        d = {}
        while queue:
            node = queue.pop(0)
            d[node.val] = d.get(node.val, 0) + 1  # 字典统计小组件，之前自己整理过的，用上了。比较酷
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        res = []
        m = max(d.values())
        for k, v in d.items():
            if v == m:
                res.append(k)
        return res
        

https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/cai-niao-ti-jie-by-guo-guo-69/

   
   
####################方法2  BST模板法
###### 以后再细究

"""
执行用时：
64 ms
, 在所有 Python3 提交中击败了
88.49%
的用户
内存消耗：
17.4 MB       ###空间复杂度为什么还是高了些？
, 在所有 Python3 提交中击败了
20.00%
的用户
"""

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        p = root
        st, res = [], []
        max_times, time = 1, 1
        pre = float("inf")
        while p or st:
            while p:
                st.append(p)
                p = p.left
            p = st.pop()
            cur = p.val
            if cur == pre:
                time += 1
            else:
                time = 1
                pre = cur
            if time == max_times:
                res.append(cur)  # 因为可能有多个元素出现次数相同，所以需要append(), 而不是覆盖
            if time > max_times:
                res = [cur] # 此时只考虑当前元素，因为它目前是出现次数最多的，所以不用res.append()
                max_times = time
            p = p.right
        return res
   
   
时间复杂度：O(N)，N为树中节点个数。
空间复杂度：最坏情况下为O(N)， 例如树畸形（树的高度为线性）或每个元素出现一次的情形。

https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/solution/zhong-xu-bian-li-tuan-mie-xi-lie-er-cha-sou-suo-sh/        
        
      
      
################方法3 
########暂时还未理解其代码，以后再细究下

https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-zhong-shu-python3zhong/
      
      
      
