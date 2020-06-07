205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true


###############方法1 利用哈希表 映射原理解决

"""
执行用时 :
44 ms
, 在所有 Python3 提交中击败了
90.46%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
8.33%
的用户
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:  # 如果s[i]不在key中，但是t[i]却在values中，此时肯定不对
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]]!=t[i]: # s[i]虽然是在dic里了，但却不是之前已有的映射关系
                    return False
        return True  #  所有不对的可能性都排除后，接下来就剩下唯一正确可能
        
 https://leetcode-cn.com/problems/isomorphic-strings/solution/ha-xi-biao-qiao-miao-jie-jue-by-jamiechen_sjtu/       
        
        
