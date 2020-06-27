653. 两数之和 IV - 输入 BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

##################方法1 DFS中序+双指针
############这种方法是最直观，最容易想到的。
#########但是时间复杂度和空间复杂度这个答主没解释，需要细究下。
########主要利用了性质：bst中序遍历就是有序数组，然后再通过首尾双指针寻找

"""
执行用时：
104 ms
, 在所有 Python3 提交中击败了
49.23%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def searchTree(root):
            if not root: return []
            return searchTree(root.left) + [root.val] + searchTree(root.right)

        nums = searchTree(root)
        i, j = 0, len(nums) - 1
        while i < j:
            total = nums[i] + nums[j]
            if total < k: i+=1
            elif total > k: j-=1
            else:
                return True
        return False


https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/solution/pythonliang-shu-zhi-he-by-jutraman/


########################方法2 集合法

"""
执行用时：
100 ms
, 在所有 Python3 提交中击败了
60.74%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        allset = set()
        return self.find(root, k, allset)

    def find(self, root, k, allset):
        if not root: return False
        if k-root.val in allset:
            return True
        allset.add(root.val)
        return self.find(root.left, k, allset) or self.find(root.right, k, allset)


https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/solution/liang-shu-zhi-he-iv-by-leetcode/

