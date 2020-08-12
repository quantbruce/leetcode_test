class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):  # 每一层的元素有多少个，就循环多少次。这里是精华, 这一行我漏写了
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left) # 这里是queue.append(), 我错写成tmp.append()
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
    
#时间复杂度 O(N)： N为二叉树的节点数量，即BFS需循环N次。
#空间复杂度 O(N)： 最差情况下，即当树为平衡二叉树时，最多有N/2个树节点同时在queue中，使用O(N)大小的额外空间。?????????????

https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/solution/mian-shi-ti-32-ii-cong-shang-dao-xia-da-yin-er-c-5/
