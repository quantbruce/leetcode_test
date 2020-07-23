###########方法1 递归法
###有两个坑，易错点已经代码中进行注释
"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
92.78%
的用户
内存消耗 :
15.3 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))   #体会下为什么要加这个list()
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()  # 结合题解PPT，在脑海中在现这行代码，体会其必要性

        recur(root, sum)
        return res
    
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/mian-shi-ti-34-er-cha-shu-zhong-he-wei-mou-yi-zh-5/
