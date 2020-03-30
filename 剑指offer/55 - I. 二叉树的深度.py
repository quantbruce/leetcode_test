class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0  # 这个0 和下面的1组合就是妙用
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = [root], 0  ### queue=[], queue.append(root) 也可以写成这样。
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp  # 这行代码放不放在for循环内部都是对的，但是放在外面效率高一些
            res += 1
        return res


链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/solution/mian-shi-ti-55-i-er-cha-shu-de-shen-du-xian-xu-bia/
