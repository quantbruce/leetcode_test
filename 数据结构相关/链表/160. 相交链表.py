编写一个程序，找到两个单链表相交的起始节点。


########方法一(长短链表相连，走过最终长度一样)
"""
执行用时 :
180 ms
, 在所有 Python3 提交中击败了
72.24%
的用户
内存消耗 :
29 MB
, 在所有 Python3 提交中击败了
5.00%
的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:  # 这行代码可以省去
            return None
        nodeA = headA
        nodeB = headB
        while(nodeA !=nodeB):
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA


https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/jiao-ni-yong-lang-man-de-fang-shi-zhao-dao-liang-2/


