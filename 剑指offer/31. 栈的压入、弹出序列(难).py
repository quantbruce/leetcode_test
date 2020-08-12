#############这个题，理解了这个思路就谈不上中等难度。属于简单

################方法1 辅助栈法
###关键一句话，辅助栈顶的元素是否等于弹处序列popped[i]
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
            while stack and j < len(popped) and stack[-1] == popped[j]: # and j<len(popped) 这个条件其实可以省略，效率更高. 因为当stack为空时，j必然已经匹配完==len(popped)-1
                stack.pop()
                j += 1
        return not stack
    
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/tan-xin-by-z1m/

