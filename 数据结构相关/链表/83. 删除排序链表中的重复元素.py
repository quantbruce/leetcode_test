83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
94.88%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
6.06%
的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head #node相当于一个游标, head则始终记录起点
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head #最后返回肯定要从起点开始返回，所以为什么开始要让head分身成node

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/pythonshan-chu-pai-xu-lian-biao-zhong-de-zhong-fu-/
