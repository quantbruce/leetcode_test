524. 通过删除字母匹配到字典里最长单词
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
示例 2:

输入:
s = "abpcplea", d = ["a","b","c"]

输出: 
"a"
说明:

所有输入的字符串只包含小写字母。
字典的大小不会超过 1000。
所有输入的字符串长度不会超过 1000。

###############方法1 暴力法

"""
执行用时：
800 ms
, 在所有 Python3 提交中击败了
19.15%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:    
        res = ""
        for str_d in d:
            j = 0
            for i in range(len(s)):
                if j < len(str_d):
                    if s[i] == str_d[j]: j+=1
                    if j == len(str_d):
                        if (len(str_d)>len(res)) or (len(str_d)==len(res) and str_d < res):
                            res = str_d
        return res
        
## 时间复杂度太高了
## 答案来源于讨论区
https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/kan-si-bu-fu-za-qi-shi-zhen-de-bu-fu-za-by-uygn9i8/
        
        
        
#################方法2 最优方法
#####但是语法有些难以理解

"""
执行用时：
80 ms
, 在所有 Python3 提交中击败了
99.19%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))#对字典d进行排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        def f(c):                   #匹配函数
            i = 0
            for j in c:             #遍历单词里的字母
                k = s.find(j, i)    #查找函数，后一个参数是查找起点
                if k == -1:
                    return False    #查找失败就返回错误
                i = k + 1           #查找成功就更新查找起点
            return True
        for c in d:                 #遍历字符串列表
            if f(c):                #如果符合验证就输出
                return c
        return ''                   #否则输出空串


https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/524-tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-dian-li-/

"""
时间复杂度： O(n \cdot x \log n + n \cdot x)O(n⋅xlogn+n⋅x) 。这里， nn 表示列表 dd 中字符串的数目，xx 表示字符串的平均长度。排序需要花费 O(n\log n)O(nlogn) 的时间， isSubsequence 函数需要花费 O(x)O(x) 的时间去检查一个字符串是否是另一个字符串的子序列。

空间复杂度： O(\log n)O(logn) 。排序平均需要 O(\log n)O(logn) 的空间。

https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-dian-li-zui-/
"""        
        
        
        
        
