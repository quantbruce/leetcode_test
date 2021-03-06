###########方法1 递归法
###把题解的几个案例在草稿纸上笔画下，举例子，按照特殊推到一般。发现规律

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        # 第一个字母是否匹配
        first_match = bool(s and p[0] in {s[0],'.'})
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":  # 对a*的处理，其实是self.isMatch(s, p[2:])，就是选择跳过a*, p后移两位。 first_match and self.isMatch(s[1:], p)是第一个元素互相匹配后，才能p后移两位
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)  # 当p[1]==*时，first_match(第一个元素)可以匹配不对，但是后面的一定要对。
        else:                                                                        # 例如，s = "aab" , p = "b*aab" 就是满足这种场景
            return first_match and self.isMatch(s[1:], p[1:])

#时间复杂度：O() ???
#空间复杂度：O(1)
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/hui-su-dong-tai-gui-hua-by-ml-zimingmeng/


################方法2 动态规划
"""
日后细究
"""
