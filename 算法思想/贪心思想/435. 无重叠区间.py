435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。


##############方法1 贪心算法

"""
执行用时：
108 ms
, 在所有 Python3 提交中击败了
27.96%
的用户
内存消耗：
16.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0

        intervals = sorted(intervals, key=lambda x: x[1])
        ans = 0 # 统计非重叠区间的个数
        end = -float('inf')
        for i in intervals: 
            if i[0] >= end: # 如果这一个区间的左端点 >= 上一个区间的右端点
                ans+=1
                end = i[1]
        return len(intervals) - ans


https://leetcode-cn.com/problems/non-overlapping-intervals/solution/python-tan-xin-onlogn-by-meng-jian-yue-qiu-de-mao/


