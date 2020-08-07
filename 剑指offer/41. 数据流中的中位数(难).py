###################方法1 Krahets 堆排序法
######方法技巧性很强，基础要比较扎实


from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A)) ###负号含义不理解，总容易混淆
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0 #(self.A[0]-self.B[0])为什么是减号？，实际上B最初也是小顶堆，
#时间复杂度：O(logN)                                                                                                          但是后面强行取反(负数)， 便转化为了大顶堆
#空间复杂度：O(N)
https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/


##################方法2 最容易最直观的排序法
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        self.store.append(num)

    def findMedian(self) -> float:
        self.store.sort()
        n = len(self.store)
        if n & 1 == 1: # n 是奇数
            return self.store[n // 2]
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) / 2
        
#时间复杂度：O(N*logN)
#空间复杂度：O(N)
# https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/you-xian-dui-lie-by-z1m/



####################方法3 二分插入法
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """       
        self.res = []

    def addNum(self, num: int) -> None:
        if not self.res:
            self.res.append(num)
        else:
            bisect.insort_left(self.res, num)

    def findMedian(self) -> float:
        n = len(self.res)
        self.res.sort()
        if n & 1==1: 
            return self.res[n//2]
        else:
            return (self.res[n//2-1]+self.res[n//2])/2

#时间复杂度：O(n)。O(logn)+O(n)≈O(n)。 其中包括： 查找元素插入位置O(logN) （二分查找）、向数组某位置插入元素O(N) （插入位置之后的元素都需要向后移动一位）。
#空间复杂度：O(n)。使用了数组保存输入。

# https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/you-xian-dui-lie-by-z1m/









