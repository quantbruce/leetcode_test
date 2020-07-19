https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/

06. 从尾到头打印链表（递归法、辅助栈法，清晰图解）
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:  # 不要再想着什么for循环了，这里是链表
            stack.append(head.val)
            head = head.next
        return stack[::-1]

#时间复杂度 O(N)： 入栈和出栈共使用 O(N)时间。
#空间复杂度 O(N)： 辅助栈 stack 和数组 res 共使用O(N)的额外空间


################方法2 递归法
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []
    
#时间复杂度 O(N)： 遍历链表，递归N次。
#空间复杂度 O(N)： 系统递归需要使用O(N)的栈空间。
