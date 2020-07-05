744. 寻找比目标字母大的最小字母
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
 

示例：

输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "d"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "g"
输出: "j"

输入:
letters = ["c", "f", "j"]
target = "j"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "k"
输出: "c"
 

提示：

letters长度范围在[2, 10000]区间内。
letters 仅由小写字母组成，最少包含两个不同的字母。
目标字母target 是一个小写字母。



##########################方法1 My Method
###就是观察样例，进行归纳

"""
执行用时：
140 ms
, 在所有 Python3 提交中击败了
50.24%
的用户
内存消耗：
14.1 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
            if i == letters[-1]:
                return letters[0]
                
# 时间复杂度: O(N)
# 空间复杂度: O(1)
                
 
 ### 进一步优化以上代码后
 
"""
执行用时：
140 ms
, 在所有 Python3 提交中击败了
50.24%
的用户
内存消耗：
14.1 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
 """
 class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target): # 实际上，字符串本身就可以比较，无需再写ord
                return i
        return letters[0]
       
       
       
### 再进一步优化后

"""
执行用时：
128 ms
, 在所有 Python3 提交中击败了
94.83%
的用户
内存消耗：
14.1 MB
, 在所有 Python3 提交中击败了
25.00%
的用户
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        return letters[0]
       
https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/solution/xun-zhao-bi-mu-biao-zi-mu-da-de-zui-xiao-zi-mu-by-/
 
 
###############################方法2 









