##李克的想法(递归思路)

def f(n, i):  # n是第n个骰子，i是骰子点数和
    if n == 1:
        if 1 <= i <= 6:
            return 1 / 6
        return 0
    else:
        return (f(n-1, i-1) + f(n-1, i-2) + f(n-1, i-3) + f(n-1, i-4) + f(n-1, i-5) + f(n-1,  i-6)) / 6

def g(n):
    ls = []
    for i in range(n, 6 * n + 1):  # 第n颗骰子的点数和范围必然落在(n, 6 * n + 1)
        ls.append(round(f(n, i), 5))
    return ls

print(g(4))



###################方法2 动态规划(滚动数组优化)

"""
执行用时：
44 ms
, 在所有 Python3 提交中击败了
54.65%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def twoSum(self, n: int) -> List[float]:
        pre = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
        for i in range(2, n+1):    # 这行代码漏写了
            tmp = [0]*(5*i+1)
            for x in range(len(pre)):
                for y in range(6):
                    tmp[x+y] += pre[x]/6
            pre = tmp
        return pre
#时间复杂度：O(N**2) 我自己的判断，O(N*(5N+1)*6)
#空间复杂度：O(N**2)  我自己的判断 一颗骰子O(5*N+1)， 推到N颗，所以应该是O(5*N+1)*O(N)
https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/java-dong-tai-gui-hua-by-zhi-xiong/
