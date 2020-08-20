#########My Methods 暴力法
"""
执行用时 :
620 ms
, 在所有 Python3 提交中击败了
25.28%
的用户
内存消耗 :
17.2 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res

#时间复杂度：？？？？？？
#空间复杂度：O(K)

#############方法2 维持一个单调递减的队列

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque=[]
        result=[]
        for i in range(len(nums)):
            # 只存有可能成为最大值数字的index进入deque
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)

            #如果相聚超过窗口长度k，丢弃掉deque中首位index
            while i-deque[0]>k-1:  # 这个while 可以改成if, 因为上面的deque.append(i)每一轮只加了一个进去
                deque.pop(0)
            # 只要满足一个窗口的长度k，就向result中添加nums[deque[0]]一个结果
            if i>=k-1:
                result.append(nums[deque[0]]) #在整个过程中，始终保持deque[0]为最大值的index
        return result
    
# 时间复杂度O(N)： 其中n为数组nums长度；线性遍历nums占用O(N)；每个元素最多仅入队和出队一次，因此单调队列deque占用O(2N) 。
# 空间复杂度O(k)： 双端队列deque中最多同时存储k个元素（即窗口大小）。


代码：    
https://blog.csdn.net/weixin_43455338/article/details/105011557
动画：
https://www.cxyxiaowu.com/1141.html

 

#############方法3 Krahets法

https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-i-hua-dong-chuang-kou-de-zui-da-1-6/
    
    
