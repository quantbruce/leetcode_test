189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]


############方法1 三次旋转法
##Tips：这个技巧性挺酷的，值得掌握。

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
92.16%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
97.30%
的用户
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 这是为了防止k大于n时的情况
        def swap(left, right):
            while left<right:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
                right -= 1    
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)

        
https://leetcode-cn.com/problems/rotate-array/solution/san-ci-fan-zhuan-fu-yi-xie-pythonicde-jie-fa-pytho/


###方法2  另外一种写法，借助python的切片完成反转。

"""
执行用时 :
32 ms
, 在所有 Python3 提交中击败了
97.90%
的用户
内存消耗 :
14 MB
, 在所有 Python3 提交中击败了
86.49%
的用户
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
一些pythonic的解法
切片


#### 方法3 

"""
执行用时 :
40 ms
, 在所有 Python3 提交中击败了
81.23%
的用户
内存消耗 :
13.9 MB
, 在所有 Python3 提交中击败了
91.89%
的用户
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]
插入


#### 方法4  插入法

"""
执行用时 :
164 ms
, 在所有 Python3 提交中击败了
5.79%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop()) # 在index=0的地方插入，相当于头插法，并不会覆盖之前index元素，只会让他不断右移

