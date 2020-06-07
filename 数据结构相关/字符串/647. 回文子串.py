647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。


"""
执行用时 :
120 ms
, 在所有 Python3 提交中击败了
92.00%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
30.77%
的用户
"""

######################方法1， 中心点两侧拓展法
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        length = len(s)
        for center in range(2*length-1):
            left = center // 2   # left,right其实只是两个下标而已
            right = left + center % 2 
            while left>=0 and right<length and s[left] == s[right]: # 只有满足s[left]==s[right] 才能够拓展
                ans += 1
                left -= 1
                right += 1
        return ans 
        
        
        ## (1)是python解的，(2)的原理讲的非常好，尤其是中心点center个数为什么等于2*N-1
        (1) https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode/
        (2) https://leetcode-cn.com/problems/palindromic-substrings/solution/liang-dao-hui-wen-zi-chuan-de-jie-fa-xiang-jie-zho/



#############方法2 动态规划法
###### 我翻译了人家的java代码(再好好吃透下)

"""
执行用时 :
280 ms
, 在所有 Python3 提交中击败了
46.46%
的用户
内存消耗 :
22.2 MB
, 在所有 Python3 提交中击败了
7.69%
的用户
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = 0

        for j in range(len(s)):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1
        return ans


https://leetcode-cn.com/problems/palindromic-substrings/solution/liang-dao-hui-wen-zi-chuan-de-jie-fa-xiang-jie-zho/











