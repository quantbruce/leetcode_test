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
########暴力法
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

  
  
  
  
  
  
        
     
