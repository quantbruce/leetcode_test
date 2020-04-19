"""
执行用时 :
84 ms
, 在所有 Python3 提交中击败了
56.23%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2: return len(s)
        res = 1
        head = tail = 0

        while tail<len(s)-1: # 因为下面马上就要tail+=1, 所以不能取等号，否则会发生越界。
            tail+=1
            if s[tail] not in s[head:tail]:
                res = max(tail-head+1, res)  # 因为实际向右滑动的过程中，窗口很可能会缩短。
            else:                            # 为了确保res的数最大，要始终确保其递增。
                while s[tail] in s[head:tail]:  # 因为窗口中相等的元素若不在左端点，则需要移动多次，所以需要while循环
                    head += 1
        return res

    
    
