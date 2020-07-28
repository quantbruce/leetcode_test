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
    
########这样更精炼   
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_former = s[:n]
        s_latter = s[n:]
        return s_latter + s_former
#时间复杂度：O(N) 仔细看解释
#空间复杂度：O(N)
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/mian-shi-ti-58-ii-zuo-xuan-zhuan-zi-fu-chuan-qie-p/
    
###########Krahets 取余法，容易理解
#########Krahets关于这题的时间复杂度和空间复杂度以及测试的代码讲解的非常好，反复多看。直到融为一体
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, n + len(s)):
            res += s[i%len(s)]
        return res
    
        
#############除余法(变相循环，也是很巧妙)
  class Solution:
    def reverseLeftWords(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        for i in range(k, k+n):
            res+=s[i%n]
        return res
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/chao-jian-dan-duo-chong-jie-fa-python3-by-azl39798/

    
    
    
    
