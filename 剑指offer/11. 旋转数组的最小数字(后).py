class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1  # 这一部的分情况讨论很见功底，多理解下，最后部分题解关于正确性的证明还没能理解。
        return numbers[i]

#时间复杂度：O(log(n)) 在特例情况下（例如 [1, 1, 1, 1]），会退化到 O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/

# 关于上述的几个if条件
# 例子[3, 4, 5, 6, 1, 2] 可解释 i = m + 1
# 例子[4, 1, 2 ,3] 可解释 j = m


