https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/

06. 从尾到头打印链表（递归法、辅助栈法，清晰图解）
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:  # 不要再想着什么for循环了，这里是链表
            stack.append(head.val)
            head = head.next
        return stack[::-1]
