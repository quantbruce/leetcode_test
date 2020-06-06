594. 最长和谐子序列
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.


###################方法1，构建哈希表，再扫描
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
           dic[i] = dic.get(i, 0) + 1  # 这是一个统计字典频数最常见的套路，需要熟练掌握。

        res = 0
        for i in dic:
            if i+1 in dic:
                res = max(res, dic[i]+dic[i+1])
        return res
        
        
https://leetcode-cn.com/problems/longest-harmonious-subsequence/solution/ha-xi-biao-by-tian-dao-yao-xing-7/
        
        
原理来源：
https://leetcode-cn.com/problems/longest-harmonious-subsequence/solution/zui-chang-he-xie-zi-xu-lie-by-leetcode/
