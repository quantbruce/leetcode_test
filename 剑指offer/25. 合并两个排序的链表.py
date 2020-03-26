class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)  # (1) dum = ListNode(0) 生成dum节点, （2）(指针)cur = dum(节点), cur指针指向dum节点。
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            elif l1.val > l2.val:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
        
        https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/solution/mian-shi-ti-25-he-bing-liang-ge-pai-xu-de-lian-b-2/
