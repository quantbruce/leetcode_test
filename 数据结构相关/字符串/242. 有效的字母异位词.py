242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


#########方法1  排序法

"""
执行用时 :
60 ms
, 在所有 Python3 提交中击败了
68.66%
的用户
内存消耗 :
14.8 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if sorted(s)!=sorted(t):
            return False
        return True



"""
执行用时 :
64 ms
, 在所有 Python3 提交中击败了
56.42%
的用户
内存消耗 :
14.8 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        
        
##########方法2 哈希表法 
### tips：注意，虽然申请了d = {}, 但这里的空间复杂度仍旧是O(1), 因为d的key再怎么样也跳不出26个字母范围

"""
执行用时 :
68 ms
, 在所有 Python3 提交中击败了
43.35%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for i in t:
            dic[i] = dic.get(i, 0) - 1
            if dic[i]<0:
                return False
        return True


https://leetcode-cn.com/problems/valid-anagram/solution/you-xiao-de-zi-mu-yi-wei-ci-by-leetcode/











