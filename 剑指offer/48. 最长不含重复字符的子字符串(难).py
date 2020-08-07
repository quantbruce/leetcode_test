###############方法1 滑动窗口法

"""
执行用时 :
84 ms
, 在所有 Python3 提交中击败了
56.23%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2: return len(s)
        res = 1
        head = tail = 0

        while tail<len(s)-1: # 因为下面马上就要tail+=1, 所以不能取等号，否则会发生越界。
            tail+=1
            if s[tail] not in s[head:tail]:
                res = max(tail-head+1, res)  # 因为实际向右滑动的过程中，窗口很可能会缩短。
            else:                            # 为了确保res的数最大，要始终确保其递增。
                while s[tail] in s[head:tail]:  # 因为窗口中相等的元素若不在左端点，则需要移动多次，所以需要while循环
                    head += 1
        return res
    
#时间复杂度：O(N**2)  尝试用abcd...z这样的例子来理解 我理解应该是挨个比较进行判断。 这样的话，tail节点要走n个，
#空间复杂度：O(1)                                 # 如果head一直不动（最坏情况，全部都不重复），那么每一次比对的次数就是1+2+...+n，复杂度就是n平方
    
    
#################方法2 滑动窗口法的优化

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        head, res = 0, 0
        hashmap = {}
        for tail in range(n):
            if s[tail] in hashmap:
                head = max(hashmap[s[tail]], head) # 如果写成 head = hashmap[s[tail]], 对于"abba"会输出3，正确答案是2
            hashmap[s[tail]] = tail + 1 # 不管在不在, tail下标都要向后移一位, 这样代码好好体会
            res = max(tail-head+1, res)
        return res

#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/tu-jie-hua-dong-chuang-kou-shuang-zhi-zhen-shi-xia/
    
    
###################方法3 Krahets法









