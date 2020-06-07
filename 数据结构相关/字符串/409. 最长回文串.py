409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
75.03%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""


#############方法1 贪心法
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1

        for v in dic.values():
            ans += v//2*2
            while ans % 2 == 0 and v % 2 == 1: # 这个循环其实只会执行一次，因为只有一个奇数次v可以放中间，再多奇数的话就够不成回文串了。
                ans += 1
        return ans


#############以下写法等价
class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = collections.Counter(s)  # 也可以用Counter()来统计字典频次
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


https://leetcode-cn.com/problems/longest-palindrome/solution/zui-chang-hui-wen-chuan-by-leetcode-solution/







