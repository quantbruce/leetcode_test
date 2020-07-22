解决思路：最先想到的是使用栈来存储链表的第一遍遍历的值。再重新遍历链表，遍历的同时弹出栈的元素（弹出的顺序刚好是链表节点值的倒序），
为当前节点赋值当前弹出的值。python可以直接使用list结构存储遍历值，读取的时候倒序读取list元素，就相当于栈的原理。

############方法1 My Method 线性扫描+辅助栈

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
    
#时间复杂度：O(N)
#空间复杂度：O(1)


############方法2 双指针法 最优
"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
97.39%
的用户
内存消耗：
14.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
#时间复杂度：O(N)
#空间复杂度：O(1)
    
    
############方法3 递归法
"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
54.13%
的用户
内存消耗：
18.4 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret
#时间复杂度：O(N)
#空间复杂度：O(N)












