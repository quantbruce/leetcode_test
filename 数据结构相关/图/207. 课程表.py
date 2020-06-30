207. 课程表
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？


示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5


#########################方法1：入度表（广度优先遍历）
########关于下标还有些未完全理解
########反复多看题解，体会解题思想

"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
80.90%
的用户
内存消耗：
14.2 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
"""

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]  # 邻接列表
        queue = deque()
        for cur, pre in prerequisites:
            indegrees[cur] += 1       #####为什么这个地方不会out of range?
            adjacency[pre].append(cur)

        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)

        while queue:
            pre = queue.popleft()
            numCourses -= 1 
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses
        
        
https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
  

###################方法2 递归法

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
92.91%
的用户
内存消耗：
16.2 MB
, 在所有 Python3 提交中击败了
11.11%
的用户
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flag):
            if flag[i]==1: return False
            if flag[i]==-1: return True
            flag[i]=1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flag): return False
            flag[i]=-1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flag = [0 for _ in range(numCourses)]   
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flag): return False
        return True

       
https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/












        
