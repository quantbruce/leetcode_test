#######My Methods

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
81.58%
的用户
内存消耗 :
13.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        res, stack = [], []
        stack = s.strip().split(" ")
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '':
                continue
            else:
                res.append(stack[i])
                
        return(' '.join(res))
        
        
        
        
        
        
        
