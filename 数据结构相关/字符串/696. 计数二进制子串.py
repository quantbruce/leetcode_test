696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。


#######################方法1 按字符分组法
"""
执行用时 :
260 ms
, 在所有 Python3 提交中击败了
42.95%
的用户
内存消耗 :
14.2 MB
, 在所有 Python3 提交中击败了
14.29%
的用户
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]  # 可以看成是频次统计表 
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                groups.append(1)
            else:
                groups[-1]+=1
        
        ans = 0
        for i in range(len(groups)-1):
            ans += min(groups[i], groups[i+1]) # 真正的精髓在此
        return ans


####################方法二
"""
执行用时 :
208 ms
, 在所有 Python3 提交中击败了
64.42%
的用户
内存消耗 :
14 MB
, 在所有 Python3 提交中击败了
14.29%
的用户
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, pre, cur = 0, 0, 1
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                ans += min(pre, cur)
                cur, pre = 1, cur # cur永远要赋初值为1，是因为一开始的当前元素，必然自成一组
            else:
                cur += 1

        return ans + min(pre, cur)



https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode/
