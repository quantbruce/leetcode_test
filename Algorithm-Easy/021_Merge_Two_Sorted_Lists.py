class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return("{}->{}".format(self.val, self.next))

class Solution(object):
    def mergeTwoList(self, l1, l2):
        '''
        :type l1: ListNode
        :tyoe l2: ListNode
        :rtype: ListNode
        ''' 
        curr = dummy = ListNode(0)   # curr相当于新的拼接合成的那个 listNode
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    a = Solution()
    print(a.mergeTwoList(l1, l2))
