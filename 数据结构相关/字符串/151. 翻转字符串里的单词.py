151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


#########方法1 双指针法

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
58.57%
的用户
内存消耗 :
13.9 MB
, 在所有 Python3 提交中击败了
10.00%
的用户
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回


https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/151-fan-zhuan-zi-fu-chuan-li-de-dan-ci-shuang-zh-2/



#######方法二  
#tips：split()法，面试尽量别用，有些调库取巧的味道

"""
执行用时 :
24 ms
, 在所有 Python3 提交中击败了
99.82%
的用户
内存消耗 :
14 MB
, 在所有 Python3 提交中击败了
10.00%
的用户
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回



#### 也可以将上述代码简化为1行
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])


https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/151-fan-zhuan-zi-fu-chuan-li-de-dan-ci-shuang-zh-2/



