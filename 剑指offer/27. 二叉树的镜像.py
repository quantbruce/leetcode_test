class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.mirrorTree(root.left)
        if root.right:  # 为什么换成elif就报错，因为if/elif两者只会走其中一条路
            self.mirrorTree(root.right)
        return root
        
        
https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/qing-xi-de-pythondai-ma-by-xiaowoniuyy/
