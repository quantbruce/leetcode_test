565. 数组嵌套
索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到并返回最大的集合S，S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

示例 1:

输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
注意:

N是[1, 20,000]之间的整数。
A中不含有重复的元素。
A中的元素大小在[0, N-1]之间。

#######方法1(哈希表法)

"""
执行用时 :
160 ms
, 在所有 Python3 提交中击败了
43.25%
的用户
内存消耗 :
17.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            d[i] = nums[i]
        count = 0
        i = 0
        while i < len(nums):
            tmp = i
            ans = 0
            while d[tmp] != '#':
                ans += 1
                res = d[tmp]
                d[tmp] = '#'
                tmp = res
            i += 1
            count = max(count,ans)
        return count

    
Tips: 不用每次都重置字典d，应为已经访问过的元素，是不会出现在其他的答案里的，比如说S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}，
      那么无论从0,5,6,2的哪一个开始找，结果多事一样的只是顺序不同，而且之后的答案里是不会出现 0,5,6,2这几个数的，
      应为一个数只能出现在一个答案里。不可能有好几个索引都指向这一个元素

https://leetcode-cn.com/problems/array-nesting/solution/python3zi-dian-by-aiyishiqu-5/


 #########方法二(更加简洁，但还没理解！)


"""
执行用时 :
148 ms
, 在所有 Python3 提交中击败了
57.67%
的用户
内存消耗 :
15.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""


def arrayNesting(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxRes = 0
    for i in range(len(nums)):
        curr, j = 0, i
        while nums[j] >= 0:
            temp = j
            j = nums[j]
            nums[temp] = -1
            curr += 1
        maxRes = max(maxRes, curr)
    return maxRes

https://unclegem.cn/2018/11/25/Leetcode%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0-565-%E6%95%B0%E7%BB%84%E5%B5%8C%E5%A5%97/



