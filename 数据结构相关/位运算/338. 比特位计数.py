338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。



##############方法1， python转移官方解答方法1
####自定义了popcount函数, 但是这个方法无论时间复杂度还是空间复杂度都是10%徘徊

"""
执行用时 :
156 ms
, 在所有 Python3 提交中击败了
21.07%
的用户
内存消耗 :
20.5 MB
, 在所有 Python3 提交中击败了
11.11%
的用户
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        def popcount(x): # 统计二进制中1个数的函数
            count = 0
            while x:
                x &= (x-1) # 还是用了这招，除掉末尾一个1，count计数一次
                count += 1
            return count

        ans = []
        for i in range(num+1):
            ans.append(popcount(i))
        return ans
        


##################方法2，动态规划法 （该法较优）
#####这个题分成了奇偶数来看，在运用了动态规划法，这个套路很经典。值得记住！

"""
执行用时 :
96 ms
, 在所有 Python3 提交中击败了
75.18%
的用户
内存消耗 :
21 MB
, 在所有 Python3 提交中击败了
11.11%
的用户
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0, 1, 1] # 体会下，起步为什么要是三个元素？其实写成 res = [0] 下面对应改成 for i in range(1, num+1): 代码也同样能通过
        for i in range(3, num+1):  # 0之所以要单独拿出来，是因为动态规划的初始条件，要点原料点火啊，对吧。体会下
            if i & 1 == 1:
                res.append(res[-1] + 1)  # 体会res[-1]，不要在python中写成res[i]=res[i-1]+1, 这种会语法报错
            else:
                res.append(res[i//2])
        return res[:num+1]  # :num+1是为了输入的数字<=3, 此时[]长度小于3, 而res=[0,1,1]     
  
  
  https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/
  
  
  
  
  
