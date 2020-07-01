141. 环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。


示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。



进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = {}
        while head:
            if head in node:
                return True
            else:
                node[head] = 1
            head = head.next
        return False
        
        
# 时间复杂度：O(N)
# 空间复杂度：O(N) 不满足进阶O(1)要求
https://leetcode-cn.com/problems/linked-list-cycle/solution/huan-xing-lian-biao-by-leetcode/
        



################方法2 快慢指针法

"""
执行用时：
60 ms
, 在所有 Python3 提交中击败了
75.32%
的用户
内存消耗：
16.7 MB
, 在所有 Python3 提交中击败了
9.52%
的用户
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        
 # 时间复杂度：O(N)
 # 空间复杂度：O(1)
        
"""
这道题好像很火啊，几个月之前做的，一直有人点赞。其实当时是我想错了，觉得快指针一直在循环会浪费时间，其实不是这样的。
这整个时间复杂度只和慢指针有关系。当慢指针进入循环圈之后，无论快指针在哪里，都是快指针去追慢指针。最好情况下，快指针在最后，
这样一步就相遇了。时间复杂度是O(n-m)m是链表的循环部分。可是最坏情况下，快指针在慢指针的前面一个位置，那么每走一次他们的距离缩小1，
所以要走m次他们才能相遇，时间复杂度是O(n)。综上，快慢指针平均情况更优，而哈希表每次都是O(n)
"""      
        
