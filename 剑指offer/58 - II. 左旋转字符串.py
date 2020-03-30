###########My Method

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
61.85%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_latter = ''.join(list(s)[n:])
        s_former = ''.join(list(s)[:n])
        return s_latter+s_former
        
        
  #############除余法(变相循环，也是很巧妙)
  class Solution:
    def reverseLeftWords(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        for i in range(k, k+n):
            res+=s[i%n]
        return res
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/chao-jian-dan-duo-chong-jie-fa-python3-by-azl39798/
