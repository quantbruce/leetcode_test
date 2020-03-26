解决思路：最先想到的是使用栈来存储链表的第一遍遍历的值。再重新遍历链表，遍历的同时弹出栈的元素（弹出的顺序刚好是链表节点值的倒序），
为当前节点赋值当前弹出的值。python可以直接使用list结构存储遍历值，读取的时候倒序读取list元素，就相当于栈的原理。



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lst = []
        temp1 = head
        while temp1:
            lst.append(temp1.val)
            temp1 = temp1.next
        i = len(lst)-1
        temp2 = head
        while i>=0:
            temp2.val = lst[i]
            temp2 = temp2.next
            i -= 1
        return head
