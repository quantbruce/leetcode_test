给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例 1：

输入: 
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。
例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
示例 2：

输入: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
 

提示:

root 的长度范围： [0, 1000].
输入的每个节点的大小范围：[0, 999].
k 的取值范围： [1, 50].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-linked-list-in-parts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
74.08%
的用户
内存消耗 :
14.1 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # 构建链表
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k) # divmod(被除数, 除数) 返回 (商, 余数)

        # 开始带条件赋值
        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None) # 头部空指针套路, head和write是指向同一个引用的
            for j in range(width + (i < remainder)): # 精髓
                write.next = ListNode(cur.val)
                write = write.next
                if cur: cur = cur.next # 因为cur.val要确保赋值也相应更新
            ans.append(head.next) # 因为 head本质上是个最开始的空节点。
        return ans                #trick: 这种在列表中，append节点，会默认增加一层[]
        
        
        https://leetcode-cn.com/problems/split-linked-list-in-parts/solution/fen-ge-lian-biao-by-leetcode-2/
        
