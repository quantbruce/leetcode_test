318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。



###############方法1 暴力集合法

"""
执行用时 :
1344 ms
, 在所有 Python3 提交中击败了
32.28%
的用户
内存消耗 :
15.4 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ws = [(set(w),len(w)) for w in words]
        res, N = 0, len(words)
        for i in range(N-1):
            for j in range(i+1, N):
                if not ws[i][0].intersection(ws[j][0]) :
                    res = max(res, ws[i][1]*ws[j][1])
        return res


https://leetcode-cn.com/problems/maximum-product-of-word-lengths/solution/qiao-yong-setwu-xu-wei-yun-suan-by-rockypan/


################方法2  官方直观法

"""
执行用时 :
1192 ms
, 在所有 Python3 提交中击败了
41.76%
的用户
内存消耗 :
14.1 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letter(s1, s2):
            for ch in s1:
               if ch in s2:
                   return False
            return True
        
        res, N = 0, len(words)
        for i in range(N-1):
            for j in range(i+1, N):
                if no_common_letter(words[i], words[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res

https://leetcode-cn.com/problems/maximum-product-of-word-lengths/solution/zui-da-dan-ci-chang-du-cheng-ji-by-leetcode/



#################方法3 超时了
理论上应该比方法二时间复杂度更低，但是却莫名超时了。。。懂位运算原理即可

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(s1, s2):
            bit_number = lambda ch : ord(ch) - ord('a')
            bitmask1 = bitmask2 = 0
            for ch in s1:
                bitmask1 |= 1 << bit_number(ch)
            for ch in s2:
                bitmask2 |= 1 << bit_number(ch)
            return bitmask1 & bitmask2 == 0

        res, N = 0, len(words)
        for i in range(N-1):
            for j in range(i+1, N):
                if no_common_letters(words[i], words[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res


















