345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。


################方法1  目标元素入栈法
### 体会下翻滚的意思，实际上就是利用了栈，单独对元音字母逆序操作

"""
执行用时：
60 ms
, 在所有 Python3 提交中击败了
84.94%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        x = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = []
        ls = [i for i in s if i in x]

        for k in s:
            if k not in x:
                res.append(k)
            else:
                res.append(ls.pop())
        return ''.join(res)

https://leetcode-cn.com/problems/reverse-vowels-of-a-string/solution/shuang-zhi-zhen-huo-zhe-lie-biao-de-popfang-fa-shi/
    
    
############方法2 双指针法 (更优)
###这两个算法的时间复杂度和空间复杂度要自己细扣下

"""
执行用时：
56 ms
, 在所有 Python3 提交中击败了
92.50%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        x = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = []
        j = len(s)-1

        for i, k in enumerate(s):
            if k in x:
                while s[j] not in x:
                    j-=1
                res.append(s[j])
                j-=1
            else:
                res.append(k)
        return ''.join(res)
    
    
    https://leetcode-cn.com/problems/reverse-vowels-of-a-string/solution/shuang-zhi-zhen-huo-zhe-lie-biao-de-popfang-fa-shi/
    
