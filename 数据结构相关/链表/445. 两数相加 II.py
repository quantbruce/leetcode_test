445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。


"""
执行用时 :
68 ms
, 在所有 Python3 提交中击败了
99.05%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
50.00%
的用户
"""

#############方法1(双栈配头插法)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:     # carry!=0的情况就是当s1和s2都同时为空时，如果最高位加起来大于10有进位carry, 
            a = 0 if not s1 else s1.pop()  # 则这个进位还要进行一个头插法, 这样答案才会对
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            
            curnode = ListNode(cur) # 头擦法还有些理解生疏，要多在草稿纸上画图理解，培养感觉。
            curnode.next = ans  # 这一轮的节点下一个，就是上一轮最后返回的答案节点
            ans = curnode
        return ans


https://leetcode-cn.com/problems/add-two-numbers-ii/solution/liang-shu-xiang-jia-ii-by-leetcode-solution/
