#############这个题，理解了这个思路就谈不上中等难度。属于简单
"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
97.29%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/tan-xin-by-z1m/

