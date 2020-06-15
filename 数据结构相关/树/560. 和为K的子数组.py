560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

################方法1 最优法：前缀和(利用字典)
"""
执行用时 :
56 ms
, 在所有 Python3 提交中击败了
96.16%
的用户
内存消耗 :
16.2 MB
, 在所有 Python3 提交中击败了
11.11%
的用户
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumArray = {0:1}
        count = 0
        prefixSum = 0
        
        for ele in nums:
            prefixSum += ele
            subArray = prefixSum - k
            if subArray in prefixSumArray:
                count += prefixSumArray[subArray]
            prefixSumArray[prefixSum] = prefixSumArray.get(prefixSum, 0) + 1        
        return count

####仔细多看多体会题解思想
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/hot-100-he-wei-kde-zi-shu-zu-python3-cong-bao-li-j/
