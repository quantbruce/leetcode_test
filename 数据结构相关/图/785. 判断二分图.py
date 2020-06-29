785. 判断二分图
给定一个无向图graph，当这个图为二分图时返回true。

如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。


示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释: 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释: 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。


################方法1 深度优先搜索着色【通过】

"""
执行用时：
196 ms
, 在所有 Python3 提交中击败了
99.37%
的用户
内存消耗：
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        color = {}
        for node in range(len(graph)): # 遍历graph中每个节点
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]: # 遍历与node相连的边节点
                        if nei not in color:
                            stack.append(nei) # 往stack里装nei节点
                            color[nei] = color[node]^1 # 确保相邻节点颜色逐个交替
                        elif color[nei] == color[node]:
                            return False
        return True


https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode/

