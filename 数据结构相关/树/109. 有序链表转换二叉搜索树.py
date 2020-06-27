109. 有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5


##########################方法1 （递归+快慢双指针法)
#########直观思路，不做任何转化，这题的时间复杂度和空间复杂度分析值得细品
#########仔细看题解的PPT，最好在稿纸上自己笔画下,
#########还有要注意的是，经实测代码发现，该题答案又不是唯一的，测试代码不通过，但是提交代码却能够accept

"""
执行用时：
92 ms
, 在所有 Python3 提交中击败了
42.78%
的用户
内存消耗：
17 MB
, 在所有 Python3 提交中击败了
85.71%
的用户
"""

class Solution:
    def findmid(self, head):
        prev_ptr = None
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:  # 当快指针本身非空且后面紧邻元素也非空时，这样就好理解了，学会这个套路。
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if prev_ptr:    # 注意此处的缩进, 之前老犯错
            prev_ptr.next = None
        return slow_ptr  # 注意此处的缩进

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return 
        mid = self.findmid(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node


https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-by-/




##########################方法2  转化数组法（典型空间换时间思路)

"""
执行用时：
72 ms
, 在所有 Python3 提交中击败了
97.30%
的用户
内存消耗：
20.1 MB
, 在所有 Python3 提交中击败了
14.29%
的用户
"""

class Solution:
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = self.mapListToValues(head)
        def convertListToBST(left, right):
            if left > right: return None 
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            if left == right: return node      # 这行代码起到提前阻断的作用，可有可无，感觉实际时间并没有降低多少    
            node.left = convertListToBST(left, mid-1)
            node.right = convertListToBST(mid+1, right)
            return node
        return convertListToBST(0, len(values)-1) 

      
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-by-/

      
      
#####################方法3 中序遍历模拟
#######日后有时间再细究
       
      
      
      
      
