######### 方法1 Krahets
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        pre.next = cur.next
        return head
    
#时间复杂度：O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/mian-shi-ti-18-shan-chu-lian-biao-de-jie-dian-sh-2/

########方法2 剑指原题意解法
"""
（以下代码由于题目类型不符无法通过，供参考）
有些难理解，日后细啃
"""
class Solution:
    def deleteNode(self, head, val):
        if head is None or val is None:
            return None
        if val.next is not None:  # 待删除节点不是尾节点
            tmp = val.next
            val.val = tmp.val
            val.next = tmp.next
        elif head == val:  # 待删除节点只有一个节点，此节点为头节点
            head = None
        else:
            cur = head    # 待删除节点为尾节点
            while cur.next != val:
                cur = cur.next
            cur.next = None
        return head
    
#时间复杂度：O(1)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/cong-on-dao-o1-by-ml-zimingmeng/

    
    
    
    
    
    
    
