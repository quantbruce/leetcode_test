91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

#############方法1 迭代法
### 本质上与动态规划思路一致

"""
执行用时：
40 ms
, 在所有 Python3 提交中击败了
82.80%
的用户
内存消耗：
13.5 MB
, 在所有 Python3 提交中击败了
6.25%
的用户
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0 # 首位数字是0，肯定全部不能翻译，则直接返回0
        pre, cur = 1, 1 
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0': # 如果第i位为0
                if s[i-1] == '1' or s[i-1] == '2': cur = pre
                else: return 0 # 无法翻译
            elif (s[i-1] == '1' or (s[i-1]=='2' and '1' <= s[i] <= '6')):
                cur = cur + pre
            pre = tmp
        return cur

#时间复杂度：O(N)
#空间复杂度：O(1)

https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/
https://leetcode-cn.com/problems/decode-ways/solution/dong-tai-gui-hua-tu-jie-by-nfgc/






