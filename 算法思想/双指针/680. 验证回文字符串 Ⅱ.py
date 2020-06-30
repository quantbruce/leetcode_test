680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。


####################方法1 双指针法

class Solution:
    def validPalindrome(self, s: str) -> bool:     
        def helper(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                else:
                    low += 1
                    high -= 1
            return True

        i, j = 0, len(s)-1
        while i<j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return helper(i+1, j) or helper(i, j-1) # 这一步理解下就好，因为最多只允许删除一个字符，实际上并没有删除，只是跳过去没考虑而已
        return True                                     # 能走到上面一步来看的话，一般i,j两个指针也很快要相遇了。
        
        
     ### 这里虽然有递归，但是空间复杂度仍然是O(1)， 好好体会下
     ### 时间复杂度也是O(N)
     
     https://leetcode-cn.com/problems/valid-palindrome-ii/solution/yan-zheng-hui-wen-zi-fu-chuan-ii-by-leetcode-solut/
        
        
