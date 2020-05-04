19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
85.70%
的用户
内存消耗 :
13.5 MB
, 在所有 Python3 提交中击败了
5.41%
的用户
"""

#################常规法(翻译官方java解答)

####体会：不足之处，扫描了接近2次链表，而不是一次解决。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = ListNode()
        first = head

        while first: # first就是为了统计出链表长度length
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length>0:
            length-=1
            first = first.next
        first.next = first.next.next
        return dummy.next #不写成head是为了防止极端情况 ListNode=[1], n=1


https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-by-l/
