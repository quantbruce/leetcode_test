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
            while i-deque[0]>k-1:
                deque.pop(0)
            # 只要满足一个窗口的长度k，就向result中添加nums[deque[0]一个结果
            if i>=k-1:
                result.append(nums[deque[0]]) #在整个过程中，始终保持deque[0]为最大值的index
        return result
    
代码：    
https://blog.csdn.net/weixin_43455338/article/details/105011557
动画：
https://www.cxyxiaowu.com/1141.html





