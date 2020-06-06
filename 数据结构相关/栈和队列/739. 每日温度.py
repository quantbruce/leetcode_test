739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。


"""
执行用时 :
508 ms
, 在所有 Python3 提交中击败了
97.58%
的用户
内存消耗 :
17.2 MB
, 在所有 Python3 提交中击败了
12.50%
的用户
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                # pop the smaller value's index
                small = stack.pop()
                res[small] = i - small
            
            # append the index of current value 
            stack.append(i)

        return res
