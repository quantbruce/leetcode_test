###############方法1 递归法
###这样的递归对仗工整好看点，我觉得比Krahets的更好理解
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:  # 判断是否是空节点
            return None
        if not root.left and not root.right: # 判断是否是叶子节点
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.mirrorTree(root.left)
        if root.right:  # 为什么换成elif就报错，因为if-elif两者只会走其中一条路
            self.mirrorTree(root.right)
        return root
#时间复杂度：O(N)        
#空间复杂度：O(N)
https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/qing-xi-de-pythondai-ma-by-xiaowoniuyy/

    
##############方法2 Krahets 递归法
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root
#时间复杂度：O(N)        
#空间复杂度：O(N)
https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/

##############方法3 Krahets 迭代法 (用栈)
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        stack = [root]
        while stack:
            node = stack.pop() # node = stack.pop(0) 这样写 就相当于队列，照样可以AC, 只是前后遍历左右子树的顺序不同了
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
#时间复杂度：O(N)        
#空间复杂度：O(N)
https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/


