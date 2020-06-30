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
