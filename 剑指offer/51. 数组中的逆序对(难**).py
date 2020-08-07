剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。


示例 1:

输入: [7,5,6,4]
输出: 5


限制：

0 <= 数组长度 <= 50000


#############方法1  My Methods 线性扫描 暴力法
"""
超时
"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    count+=1
        return count

#时间复杂度: O(N^2)
#空间复杂度：O(1)


##############方法2 归并排序 官方

"""
执行用时：
1652 ms
, 在所有 Python3 提交中击败了
66.37%
的用户
内存消耗：
18.6 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l>=r: return 0
        mid = (l+r)//2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid+1, r) # inv_count的初值在这里已经默认递归到最底层时，设置为了inv_count=0
        i, j, pos = l, mid+1, l # l和mid+1分别是左右两个子数组的start下标
        while i<=mid and j<=r:
            if nums[i]<=nums[j]:               
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j-(mid+1)) 
            else:
                tmp[pos] = nums[j]
                j+=1
            pos+=1

        for k in range(i,mid+1):  # 不是很理解接下来这两个for循环, 相当于上面左右两个区间[l, mid] [mid+1, r]一部分指针遍历完了，另一部分指针还没走完。就是这种断尾的情况
            tmp[pos] = nums[k]
            inv_count += (j - (mid+1))
            pos += 1

        for k in range(j, r+1): # 这里是r+1，写错过
            tmp[pos] = nums[k]
            pos+=1
        nums[l:r+1] = tmp[l:r+1]  # 覆盖了原数组，为什么要这一行？， 不写成nums = tmp是为了防止生成新的对象
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)             
        tmp = [0] * n             # 因为相当于给nums弄了个分身的感觉
        return self.mergeSort(nums, tmp, 0, n-1)
    
#时间复杂度: O(N*log(N))
#空间复杂度: O(N)

https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/


