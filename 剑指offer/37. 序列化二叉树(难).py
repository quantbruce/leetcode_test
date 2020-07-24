################方法1 BFS
###整体思路不算难，但是涉及到两个函数，且中间部分很多细节容易出错
###仔细看题解，反复看，体会！

"""
执行用时：
160 ms
, 在所有 Python3 提交中击败了
51.10%
的用户
内存消耗：
18.5 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ",".join(res) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return 
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if vals[i]!='null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i+=1
            if vals[i]!='null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i+=1
        return root

https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/


