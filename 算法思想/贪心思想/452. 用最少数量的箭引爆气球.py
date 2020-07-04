452. 用最少数量的箭引爆气球
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

Example:

输入:
[[10,16], [2,8], [1,6], [7,12]]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。

"""
执行用时：
512 ms
, 在所有 Python3 提交中击败了
74.10%
的用户
内存消耗：
18.9 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        first_end = points[0][1]
        arrow = 1
        for x_start, x_end in points:
            if first_end < x_start:
                arrow += 1
                first_end = x_end
        return arrow 
        
https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/yong-zui-shao-shu-liang-de-jian-yin-bao-qi-qiu-b-2/
        
        
"""
贪心算法真的很多时候要靠猜，先猜可不可以用贪心算法，然后尝试举出反例，如果举不出反例，再去编码验证贪心算法是否有效。

我觉得掌握到这个程度就可以应付普通的面试了，和对待「时间复杂度」的准确验证一下，我们只需要有个感性的认识即可，具体想了解的话可能得看一些专业著作。就会有点晕了。
"""
        
