210. 课程表 II
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]] 
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。


###################方法1 BFS迭代框架
#######自己仿照207题框架，稍作修改写的

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
65.59%
的用户
内存消耗：
14.4 MB
, 在所有 Python3 提交中击败了
28.57%
的用户
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegress = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        res = []
        for cur, pre in prerequisites:
            indegress[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(indegress)):
            if not indegress[i]: queue.append(i)
        while queue:
            pre = queue.popleft()
            numCourses-=1 # 这行代码主要用来判断是否有环，有环的话numCourses永远不会等于0
            res.append(pre)
            for cur in adjacency[pre]:
                indegress[cur]-=1
                if not indegress[cur]: queue.append(cur)
        return res if not numCourses else []
        


#################方法2 递归法 DFS
#######日后再细究


