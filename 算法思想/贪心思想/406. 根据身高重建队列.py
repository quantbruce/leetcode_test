406. 根据身高重建队列
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


###############################方法1 排序+插入法
####这个题规律有点难发现，要多啃多体会下啊

"""
执行用时：
140 ms
, 在所有 Python3 提交中击败了
31.27%
的用户
内存消耗：
14.2 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

#时间复杂度：O(N^2) ??? 细究下？
#空间复杂度：O(N)

https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/
