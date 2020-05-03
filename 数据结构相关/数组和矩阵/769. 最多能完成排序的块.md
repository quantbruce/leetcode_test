数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。



#########方法1(遍历比较)

思路：一个区间内最大的数字，不应该大于这个区间最右边的index。因此我们从左向右遍历，
      如果已经观测到的最大值小于等于这个区间的index，则可以划分区间。


"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
74.90%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
16.67%
的用户
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, max_val = 0, arr[0]
        for i, num in enumerate(arr):
            if num > max_val:
                max_val = num
            if max_val == i:
                res += 1
        return res


https://github.com/marsXyr/Leetcode_python/blob/master/*769_medium_%E6%9C%80%E5%A4%9A%E8%83%BD%E5%AE%8C%E6%88%90%E6%8E%92%E5%BA%8F%E7%9A%84%E5%9D%97.md

