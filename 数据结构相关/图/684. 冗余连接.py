684. 冗余连接
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:

输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。
更新(2017-09-26):
我们已经重新检查了问题描述及测试用例，明确图是无向 图。对于有向图详见冗余连接II。对于造成任何不便，我们深感歉意。



#######################方法1 并查集

"""
执行用时：
72 ms
, 在所有 Python3 提交中击败了
64.05%
的用户
内存消耗：
14.2 MB
, 在所有 Python3 提交中击败了
20.00%
的用户
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vector = [i for i in range(len(edges)+1)]
        def find_origin(num):
            n = num
            while n != vector[n]:
                n = vector[n]
            return n
        
        for info in edges:
            o1 = find_origin(info[0])
            o2 = find_origin(info[1])
            if o1 == o2: 
                return info
            vector[o1] = vector[o2] # 合并集合
            

#### 解答来源于下面评论区
https://leetcode-cn.com/problems/redundant-connection/solution/tong-su-jiang-jie-bing-cha-ji-bang-zhu-xiao-bai-ku/  
            
时间复杂度：O(N\alpha(N)) \approx O(N)O(Nα(N))≈O(N)。其中， NN 是图中顶点的数目（以及边的数目），\alphaα 是 Inverse-Ackermann 函数。我们对 dsu.union 进行了多达 NN 次查询，这需要花费 O(\alpha(N))O(α(N)) 时间。可以去查阅资料为什么 dsu.union 具有 O(\alpha(N))O(α(N)) 复杂性、Inverse-Ackermann 函数是什么以及为什么 O(\alpha(N))O(α(N)) 大约是 O(1)O(1) 的原因。
空间复杂度：O(N)O(N)，图的当前构造（嵌入在我们的 DSU 结构中）最多有 NN 个结点。



