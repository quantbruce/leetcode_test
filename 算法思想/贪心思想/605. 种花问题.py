605. 种花问题
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。



######## 方法1 左右区间补0法
####该法很巧妙，效率也高

"""
执行用时：
200 ms
, 在所有 Python3 提交中击败了
79.26%
的用户
内存消耗：
14 MB
, 在所有 Python3 提交中击败了
10.00%
的用户
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:  # 连续三个0则可以种一盆花
                n-=1
                flowerbed[i]=1
        return n<=0
        
https://leetcode-cn.com/problems/can-place-flowers/solution/lian-xu-san-ge-0ze-ke-yi-chong-yi-pen-hua-by-ya-le/
        

#################方法2 官方题解法

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0, count = 0
        while i<len(flowerbed):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]=0) and\  # 不知道为什么这行代码java转译python就报错
                (i==len(flowerbed)-1 or flowerbed[i+1]=0):
                flowerbed[i]=1
                count+=1
            i+=1
        return count>=n
        
https://leetcode-cn.com/problems/can-place-flowers/solution/chong-hua-wen-ti-by-leetcode/
