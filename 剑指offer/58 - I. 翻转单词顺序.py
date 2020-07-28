###################My Methods

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
        
 https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/po-su-fa-xiao-bai-by-quantbruce/
    
    
    
#####################最简洁代码 
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/2ci-fan-zhuan-by-xilepeng/

    
    
##############方法2 双指针法 Krahets
###PPT脑壳放动画
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ": i -= 1 # 用while或if的时候，问下自己是一次还是多次？此处多次犯错，自己要谨记！
            res.append(s[i + 1: j + 1])
            while s[i] == " ": i -= 1 # 用while或if的时候，问下自己是一次还是多次？
            j = i
        return " ".join(res)
    
#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/mian-shi-ti-58-i-fan-zhuan-dan-ci-shun-xu-shuang-z/
    
    
###################面试撞枪口法    
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回
#时间复杂度：Krahets分析得非常好，多去看下体会下
#空间复杂度：O(N)
https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/mian-shi-ti-58-i-fan-zhuan-dan-ci-shun-xu-shuang-z/
      
