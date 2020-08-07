"""
执行用时 :
72 ms
, 在所有 Python3 提交中击败了
29.94%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""
########方法1 两次线性扫描暴力法
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        n = len(nums)
        if n==0:
            return ""
        for i in range(n):
            nums[i] = str(nums[i])    
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(nums)
    
#时间复杂度：O(N**2)
#空间复杂度：O(1)
  
  
"""
执行用时 :
52 ms
, 在所有 Python3 提交中击败了
66.27%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
  """
#########快速法
class cmpSmaller(str):
    def __lt__(self, y):
        return self + y < y + self  # 字符串拼接比较(两两比较)
# 按由小到大来排列

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        res=sorted(map(str, nums),key=cmpSmaller)
        smallest = ''.join(res)
        return smallest

https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/python3jian-dan-chu-li-by-bigkjp97/
https://blog.csdn.net/LaoYuanPython/article/details/95218694  # python中的富比较方法 __lt__  __gt__
https://blog.csdn.net/besmarterbestronger/article/details/101217761  # python中的富比较方法案例
  
  
##########快速排序递归写法 Krahets方法另写 最优
"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
58.62%
的用户
内存消耗：
14 MB
, 在所有 Python3 提交中击败了
5.47%
的用户

"""
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        def quick_sort(left, right):
            if left >= right: return
            low, high = left, right
            pivot = arr[left]
            while left < right:
                while left < right and arr[right]+pivot >= pivot+arr[right]: right-=1
                arr[left] = arr[right]
                while left < right and arr[left]+pivot <= pivot+arr[left]: left+=1
                arr[right] = arr[left]
            arr[left] = pivot
            quick_sort(low, left-1)
            quick_sort(right+1, high)
        quick_sort(0, len(nums)-1)
        return ''.join(arr)
    
#时间复杂度：O(N*logN)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/shi-fen-rong-yi-li-jie-de-jie-fa-by-wojiushigaojie/
  
  
        
     
