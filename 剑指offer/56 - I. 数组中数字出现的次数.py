##################自己独立思考下，很快解答出的一题，而且接近双百，再接再厉。保持进步！

"""
执行用时 :
48 ms
, 在所有 Python3 提交中击败了
96.73%
的用户
内存消耗 :
14.9 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

首先想到字典的key都是唯一的(字典特性)，便可已利用key记录nums中独立元素，而对应的value则作为该key的出现次数，然后分成两个阶段解题：
1）首先是通过遍历nums列表的所有元素，若元素字典中没有，则将其导入字典dic作为key, value赋值1; 若字典中已经出现过该元素，则直接在之前value上 +1即可；
2）通过遍历1）处理完毕的字典dic, 将统计次数value为1的key, 添加到结果数组res中，即完成解答。

不足：空间复杂度过高, 暂时还没想到其他好办法。抛砖引玉, 欢迎提供优化建议。

作者：quantbruce
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/jie-jin-shuang-100-zi-dian-si-lu-jian-dan-yi-li-ji/


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]]+=1 
                            
        res = []
        for key, value in dic.items():
            if value == 1:
                res.append(key)
        return res
#时间复杂度：O(N)
#空间复杂度：O(N)
    
其实可以在第一次遇见的时候在字典建立key和value，第二次遇见的时候直接删掉（因为重复数字只会出现两次），这样遍历完列表之后直接获取字典中剩下的key就可以了。我也是这么做的，不过似乎用字典就没办法达到题目要求的空间O(1)了。

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                del dic[num]
        return list(dic.keys())

############### 方法3 位运算法

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        a = b = 0
        for num in nums:
            ret ^= num
        h = 1
        while ret&h==0:
            h <<= 1
        for num in nums:
            if num & h==0:
                a^=num
            else:
                b^=num
        return [a, b]
    
#时间复杂度：O(N)
#空间复杂度：O(1)
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/

    
