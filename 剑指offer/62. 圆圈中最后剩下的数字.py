#############约瑟夫环问题
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        final_index = 0
        for len_num in range(2, n+1): # i是数组长度
            final_index = (final_index+m)%len_num
        return final_index
        
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-by-lee/
