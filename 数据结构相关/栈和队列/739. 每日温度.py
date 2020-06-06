739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。


######################方法1，(递减堆栈)

#tips: 认真看那个动画，草稿纸上多笔画。

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
        res = [0] * len(T)  # 这下为最后的元素为0买下伏笔
        stack = []  # stack在这里主要是记录T[]中要比较元素的下标的

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]: # 如果stack不为空，且要进行比较的最新元素>之前栈stack的栈顶元素stack[-1]
                # pop the smaller value's index
                small = stack.pop()  # small是个满足题设要求的栈顶元素下标
                res[small] = i - small # i - small是比较的次数，也是首次要大的元素相隔的距离
            
            # append the index of current value 
            stack.append(i)

        return res
    
    
    https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/
        
        
        
