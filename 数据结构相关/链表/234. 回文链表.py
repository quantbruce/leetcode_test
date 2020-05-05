234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


"""
执行用时 :
80 ms
, 在所有 Python3 提交中击败了
71.53%
的用户
内存消耗 :
24.1 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

###########方法1，(链表元素先都倒入数组，然后再对数组用首尾双指针)

####体会：美中不足，空间复杂度是O(n)

def isPalindrome(self, head: ListNode) -> bool:
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]


https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode/


##########方法二(递归) 讲解的非常好，要理解透彻递归的底层原理
"""
执行用时 :
104 ms
, 在所有 Python3 提交中击败了
30.09%
的用户
内存消耗 :
75.9 MB
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
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer=head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next): # 防止不是回文数时，不再更深入的遍历元素。即使止损。
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return recursively_check()

https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode/
    
    
    

##########方法三(避免使用 O(n)额外空间的方法就是改变输入。) 最优方法




















