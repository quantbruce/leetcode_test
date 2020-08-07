############## 方法1：后序遍历 + 剪枝 （从底至顶） 最优
### 见-1则不平衡，记套路
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1   ####left==-1的-1是来自于上一轮的下面else -1 返回的-1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right)+1 if abs(left-right)<=1 else -1
        return recur(root)!=-1
    
#时间复杂度：O(N) N 为树的节点数；最差情况下，需要递归遍历树的所有节点。
#空间复杂度：O(N) 最差情况下（树退化为链表时），系统递归需要使用O(N)的栈空间
https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/


    
#############方法二：先序遍历 + 判断深度 （从顶至底）
###容易想到，但是容易产生大量重复计算，低效.

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

#时间复杂度：O(N*log(N)) 需要仔细多理解下
#空间复杂度：O(N)
https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/


