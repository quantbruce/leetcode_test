337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.


#####################方法1：暴力法，

"""
体会下思想就好，实际代码python3是超时的
"""

class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}
    
        def robInternal(root, memo):
            if not root: return 0
            if memo.get(root): return memo[root]
            money = root.val
            if root.left:
                money+=(robInternal(root.left.left,memo)+robInternal(root.left.right,memo))
            if root.right:
                money+=(robInternal(root.right.left,memo)+robInternal(root.right.right,memo))
            res = max(money, robInternal(root.left,memo)+robInternal(root.right,memo))
            memo[root] = res
            return res

        return robInternal(root, memo) 


######################方法2：记忆化 - 解决重复子问题
####对方法1性能的优化，速度进一步提升，但可以看的
####出，绝对时间比Java还是慢上不少

"""
执行用时 :
56 ms
, 在所有 Python3 提交中击败了
91.16%
的用户
内存消耗 :
16.3 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}
    
        def robInternal(root, memo):
            if not root: return 0
            if memo.get(root): return memo[root]
            money = root.val
            if root.left:
                money += (robInternal(root.left.left, memo) + robInternal(root.left.right, memo))
            if root.right:
                money += (robInternal(root.right.left, memo) + robInternal(root.right.right, memo))
            res = max(money, robInternal(root.left, memo) + robInternal(root.right, memo))
            memo[root] = res
            return res  # 一定要记得写个出口返回值，不然递归会一直执行下去
           
        return robInternal(root, memo) 
        
        
https://leetcode-cn.com/problems/house-robber-iii/solution/san-chong-fang-fa-jie-jue-shu-xing-dong-tai-gui-hu/ 
        
###################方法三，继续优化(最优法)
#####体会：这个思路比较有新意，代码也简介，但是要理解需要难点。

"""
执行用时 :
56 ms
, 在所有 Python3 提交中击败了
91.16%
的用户
内存消耗 :
15.6 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if not root: return [0, 0]
            res = [0, 0]
            left = helper(root.left)
            right = helper(root.right)

            res[0] = max(left[0], left[1]) + max(right[0], right[1])  # 当前节点选择不偷时，两个孩子节点只需要拿最多的钱出来就行
            res[1] = left[0] + right[0] + root.val                    # (两个孩子节点偷不偷没关系)，这里之前没想通，好好体会下！
            return res
        ans = helper(root)
        return max(ans[0], ans[1]) 


https://leetcode-cn.com/problems/house-robber-iii/solution/san-chong-fang-fa-jie-jue-shu-xing-dong-tai-gui-hu/ 


##################方法4 动态规划








